import pytest
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
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


def test_video_player_from_community(app):
    email = app.community_board.get_admin_email()
    company_name = 'Oxford'

    app.session.login(email=email, password=app.community_board.get_admin_password())

    assert len(app.community_board.get_video_list_href()) > 0

    app.community_board.get_video_list_href().pop().click()

    expected_video_player_url = app.company_board.get_company_prefix(company_name) + app.get_server_url() + \
                           app.video_player.get_video_player_path()

    print ("expected URl: %s, actual URL: %s" % (expected_video_player_url, app.driver.current_url))
    assert (app.driver.current_url.find(app.add_protocol_to_url(expected_video_player_url.lower())) == 0)

    assert (app.video_player.get_logged_in_user_email() == email)
    assert (app.get_footer_text() == app.get_expected_footer_text())
    assert (app.get_footer_link() == app.get_expected_footer_link())
    video_source = app.video_player.get_video_src()
    assert (len(video_source) > 0)
    assert (video_source.find(app.video_player.get_video_file_name()) > 0)


def test_video_player_from_community_landing(app):
    email = app.company_board.get_admin_email()
    company_name = 'Oxford'
    community_name = 'test'

    app.session.login(email=email, password=app.company_board.get_admin_password())

    print(str(app.company_board.get_item_from_dashboard_list(community_name).text))
    ActionChains(app.driver).move_to_element(app.company_board.get_community_landing_home(community_name)).perform()
    print(str(app.company_board.get_item_from_dashboard_list(community_name).text))
    community_landing = WebDriverWait(app.driver, 5).until(expected_conditions.visibility_of
                                                           (app.company_board.get_community_landing_home(community_name)))
    print(str(app.company_board.get_item_from_dashboard_list(community_name).text))
    community_landing.click()

