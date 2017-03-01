import pytest

from Application.application import Application


fixture = None

@pytest.fixture(scope="module")
def app():
    """Create fixture"""
    global fixture
    fixture = Application('test')
    return fixture


@pytest.fixture(scope="session", autouse=True)
def close(request):
    """Destroy fixture"""
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture