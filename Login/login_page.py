from selenium import webdriver

TEST_SERVER_URL = 'http://onedayweb-test.us-west-2.elasticbeanstalk.com/'

PAGE_PATH = '/Account/Login?returnUrl=%2F'

EMAIL_FIELD_ID = 'Email'
PASSWORD_FIELD_ID = 'Password'

SUBMIT_BTN_XPATH = '//div/button[@type="submit"]'

FOOTER_TEXT_XPATH = '//footer//section[2]/p'
FOOTER_LINK_XPATH = '//footer//section[2]/p/a'


class LoginPage:

    def __init__(self):
        self.driver = webdriver.Chrome('C:/Users/tsaytieva/Documents/Python/OneDayCMS/Tools/chromedriver.exe')

    def get(self):
        """ Load login page """
        self.driver.get(TEST_SERVER_URL + PAGE_PATH)

    def login(self, email, password):
        """ Login with credentials """
        email_field = self.driver.find_element_by_id(EMAIL_FIELD_ID)
        email_field.send_keys(email)

        password_field = self.driver.find_element_by_id(PASSWORD_FIELD_ID)
        password_field.send_keys(password)

        submit_btn = self.driver.find_element_by_xpath(SUBMIT_BTN_XPATH)
        submit_btn.click()

    def get_footer_text(self):
        return self.driver.find_element_by_xpath(FOOTER_TEXT_XPATH).text

    def get_footer_link(self):
        return self.driver.find_element_by_xpath(FOOTER_LINK_XPATH).get_attribute('href')
