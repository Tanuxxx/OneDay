from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from OneDay.Application.dashboard import Dashboard
import time

COMPANY_BOARD_PATH = '/Admin/Community/Community'
ADMIN_EMAIL = 'CompanyAdmin@oxford.com'
ADMIN_PASSWORD = '12345678'
COMMUNITY_LANDING_HOME_XPATH = '//a[@class="pointer"]/span'

TOP_DASHBOARD_BTN_XPATH = '//header//div[@class="row"]//div[@class="dropdown"][1]'
TOP_APP_BTN_XPATH = '//header//div[@class="row"]//div[@class="dropdown"][2]'
TOP_APP_BTN_CONTAINER_XPATH = './div[@class="dropdown-content border-1"]'
TOP_APP_BTN_CONTENT_XPATH = './a'
TOP_WEB_BTN_XPATH = '//header//div[@class="row"]//div[@class="dropdown"][3]'


class CompanyDashboard(Dashboard):
    def __init__(self, app):
        super().__init__(app)
        self.admin_email = ADMIN_EMAIL
        self.admin_password = ADMIN_PASSWORD
        self.page_header_xpath = '//div/h2[@class="admin-header ng-binding"]'
        #self.dashboard_items_list_xpath = '//tr/td//p/a'
        self.dashboard_items_list_name_xpath = './td//p/a'
        self.dashboard_items_list_xpath = '//tr[@class="ng-scope"]'

    def get_company_name(self, name):
        return name.lower().capitalize()

    def get_company_prefix(self, name):
        return name.lower() + '.'

    def get_company_board_path(self):
        return COMPANY_BOARD_PATH

    def get_community_landing_home(self, community_name):
        community_element = self.get_item_from_dashboard_list(community_name)
        return community_element.find_element_by_xpath(COMMUNITY_LANDING_HOME_XPATH)

    def go_to_dashboard(self):
        return self.app.driver.find_element_by_xpath(TOP_DASHBOARD_BTN_XPATH).click()

    def go_to_web(self):
        return self.app.driver.find_element_by_xpath(TOP_WEB_BTN_XPATH).click()

    def go_to_app_item(self, item_name):
        app_btn = self.app.driver.find_element_by_xpath(TOP_APP_BTN_XPATH)
        mouse_hover = ActionChains(self.app.driver).move_to_element(app_btn).perform()

        app_btn_container = WebDriverWait(self.app.driver, 5).until(expected_conditions.visibility_of
                                                               (app_btn.find_element_by_xpath(TOP_APP_BTN_CONTAINER_XPATH)))
        app_btn_content = app_btn_container.find_elements_by_xpath(TOP_APP_BTN_CONTENT_XPATH)

        while app_btn_content:
            cur_el = app_btn_content.pop()
            if cur_el.text == item_name:
                item = cur_el
                break
        item.click()
