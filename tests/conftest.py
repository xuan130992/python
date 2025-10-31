import os

import pytest
from dotenv import load_dotenv
from datetime import datetime
from pytest_html import extras
import base64


from config_pack.environment import EnvConfig


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args):
    return{
        **browser_type_launch_args,
        "headless": False,
        "slow_mo": 500,
    }
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return{
        **browser_context_args,
        "storage_state":"./auth/storage_state.json",
    }
def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="qa",help="Env to run tests:qa"

    )
@pytest.fixture(scope="session", autouse=True)
def load_env(request):
    env_name = request.config.getoption("--env").lower()
    os.environ["ENV"] = env_name
    dotenv_file =f".env.{env_name}"
    print(f"\n Loading env: {dotenv_file}")
    if os.path.exists(dotenv_file):
        load_dotenv(dotenv_file,override=True)
    else:
        raise FileNotFoundError(f"env file not found: {dotenv_file}")
    return EnvConfig()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Lấy kết quả test
    outcome = yield
    rep = outcome.get_result()

    # Chỉ chụp hình khi test fail
    if rep.when == "call" and rep.failed:
        page = getattr(item, "page", None)
        if not page:
            return

        # Tạo folder screenshots
        screenshot_dir = os.path.join(os.getcwd(), "screenshots")
        os.makedirs(screenshot_dir, exist_ok=True)

        # Tên file có timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{timestamp}.png")

        try:
            page.screenshot(path=screenshot_path)
            print(f" Screenshot saved to: {screenshot_path}")
        except Exception as e:
            print(f" Failed to take screenshot: {e}")
            return

        #  Gắn hình vào report dưới dạng base64 (để nhúng thẳng vào HTML)
        if item.config.pluginmanager.hasplugin("pytest_html"):
            with open(screenshot_path, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
            from pytest_html import extras
            extra = getattr(rep, "extra", [])
            extra.append({
                "name": "Screenshot",
                "format": "html",
                "content": f'<div><img src="data:image/png;base64,{encoded_string}" '
               f'style="width:400px;height:auto;" alt="screenshot"></div>'
            })
            rep.extra = extra



@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    """Thêm biểu tượng cho pass/fail/skipped trong report HTML"""
    if report.passed:
        status_icon = '<div class="passed">PASSED</div>'
    elif report.failed:
        status_icon = '<div class="failed">FAILED</div>'
    else:
        status_icon = '<div class="skipped">SKIPPED</div>'

    if len(cells) > 1:
        cells.insert(1, status_icon)
    else:
        cells.append(status_icon)

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(1, '<th>Status</th>')

@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_html(report, data):
    """Gắn screenshot vào vùng chi tiết trong report HTML"""
    if hasattr(report, "extra"):
        for extra in report.extra:
            if extra.get("format") == "html":
                data.append(extra["content"])