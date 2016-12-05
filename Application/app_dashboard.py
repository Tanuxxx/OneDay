from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from Application.dashboard import Dashboard

TOP_APP_BTN_XPATH = '//header//div[@class="row"]//div[@class="dropdown"][2]'
TOP_APP_BTN_CONTAINER_XPATH = './div[@class="dropdown-content border-1"]'
TOP_APP_BTN_CONTENT_XPATH = './a'


class AppDashboard(Dashboard):
    def __init__(self, app):
        super().__init__(app)
        self.page_header_xpath = '//div/h2[@class="admin-header"]'
        self.dashboard_items_list_name_xpath = './td//p/a'
        self.dashboard_items_list_xpath = '//tr[@class="ng-scope"]'
        self.dashboard_title_xpath = '//div[@id="body"]//div[@class="primary background"]/p'
        self.dashboard_items_list_xpath = '//div[@id="body"]//div[contains(@class, "ng-scope")]'
        self.dashboard_items_list_name_xpath = './/p/a'

    def go_to_app_item(self, item_name):
        app_btn = self.app.driver.find_element_by_xpath(TOP_APP_BTN_XPATH)
        ActionChains(self.app.driver).move_to_element(app_btn).perform()

        app_btn_container = WebDriverWait(self.app.driver, 5).until(expected_conditions.visibility_of
                                                               (app_btn.find_element_by_xpath(TOP_APP_BTN_CONTAINER_XPATH)))
        app_btn_content = app_btn_container.find_elements_by_xpath(TOP_APP_BTN_CONTENT_XPATH)

        while app_btn_content:
            cur_el = app_btn_content.pop()
            if cur_el.text == item_name:
                item = cur_el
                break
        item.click()
