import pytest
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