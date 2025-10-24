import os

import pytest
from dotenv import load_dotenv

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

