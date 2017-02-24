
from OneDay.Application.dashboard import Dashboard
import time

COMPANY_BOARD_PATH = '/Admin/Community/Community'
ADMIN_EMAIL = 'CompanyAdmin@oxford.com'
ADMIN_PASSWORD = '12345678'
COMMUNITY_LANDING_HOME_XPATH = '//a[@class="pointer"]/span'


class CompanyDashboard(Dashboard):
    def __init__(self, app):
        super().__init__(app)
        self.admin_email = ADMIN_EMAIL
        self.admin_password = ADMIN_PASSWORD
        self.page_header_xpath = '(//div/h2[@class="admin-header ng-binding"])[2]'
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





