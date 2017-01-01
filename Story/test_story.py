import pytest
import time

from OneDay.Application.application import Application

fixture = None


@pytest.fixture
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


def test_story_dashboard(app):
    email = app.company_board.get_admin_email()

    company_name = 'Oxford'

    app.session.login(email=email, password=app.company_board.get_admin_password())

    app.story_board.go_to_dashboard()


    # expected_company_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
    #                        app.company_board.get_company_board_path()
    #
    # assert(app.driver.current_url == app.add_protocol_to_url(expected_company_url))