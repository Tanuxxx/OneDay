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

    app.story_board.go_to_app_item(app.story_board.get_story_name_in_app_box())

    expected_company_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
                           app.story_board.get_story_board_path()

    print("expected url %s = actual url %s" % (expected_company_url, app.driver.current_url))

    assert(app.driver.current_url == app.add_protocol_to_url(expected_company_url))
    assert(app.story_board.logo_is_displayed())
    assert(app.story_board.get_page_header() == "Stories")
    assert(app.session.get_logged_in_user_email() == email)
    # assert app.story_board.get_dashboard_title() == "Story", 'Assert header'
    # assert(len(app.story_board.get_dashboard_items_names_list()) > 0)