
LOGO_ID = 'logo'
TOP_DASHBOARD_BTN_XPATH = '//header//div[@class="row"]//div[@class="dropdown"][1]'

TOP_WEB_BTN_XPATH = '//header//div[@class="row"]//div[@class="dropdown"][3]'


class Dashboard:
    def __init__(self, app):
        self.app = app
        self.dashboard_title_xpath = '//table/tbody/tr/th[1]'
        self.page_header_xpath = '//div/h2[@class="admin-header color primary"]'
        #self.dashboard_items_list_xpath = '//tr/td/p/a'
        self.dashboard_items_list_xpath = '//tr[@class ="ng-scope"]'
        self.dashboard_items_list_name_xpath = './td/p/a'
        self.admin_email = None
        self.admin_password = None

    def get_admin_email(self):
        return self.admin_email

    def get_admin_password(self):
        return self.admin_password

    def logo_is_displayed(self):
        try:
            return self.app.driver.find_element_by_id(LOGO_ID).is_displayed()
        except:
            return False

    def get_page_header(self):
        return self.app.driver.find_element_by_xpath(self.page_header_xpath).text

    def get_dashboard_title(self):
        return self.app.driver.find_element_by_xpath(self.dashboard_title_xpath).text

    def get_dashboard_items_list(self):
        return self.app.driver.find_elements_by_xpath(self.dashboard_items_list_xpath)

    def get_dashboard_items_names_list(self):
        companies_list = self.get_dashboard_items_list()
        company_name_list = []

        while companies_list:
            company_name_list.append(companies_list.pop().find_element_by_xpath(self.dashboard_items_list_name_xpath).text)

        # company_name_list.reverse()
        return company_name_list

    def get_item_from_dashboard_list(self, item_name):
        companies_list = self.get_dashboard_items_list()

        while companies_list:
            current_company = companies_list.pop()
#            if (current_company.text == item_name):
            if (current_company.find_element_by_xpath(self.dashboard_items_list_name_xpath).text == item_name):
                return current_company
        return None

    def go_to_dashboard(self):
        return self.app.driver.find_element_by_xpath(TOP_DASHBOARD_BTN_XPATH).click()

    def go_to_web(self):
        return self.app.driver.find_element_by_xpath(TOP_WEB_BTN_XPATH).click()


