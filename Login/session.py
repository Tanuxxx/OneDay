
LOGIN_PATH = '/Admin/Account/Login'

EMAIL_FIELD_ID = 'Email'
PASSWORD_FIELD_ID = 'Password'

SUBMIT_BTN_XPATH = '//div/button[@type="submit"]'

USER_EMAIL_XPATH = '//div/a'
SIGN_OUT_LINK_XPATH = '//div/a[@href = "/Home/Logoff"]'

LOGGED_IN_USER_EMAIL_XPATH = '//header//div[@class="user col-sm-2 text-right-sm"]//div[@class="dropdown"]'


class Session:

    def __init__(self, app):
        self.app = app

    def get_login_url(self):
        """ Load login page """
        self.app.driver.get(self.app.get_server_cms_url() + LOGIN_PATH)

    def login(self, email, password):
        """ Login with credentials """
        self.get_login_url()

        email_field = self.app.driver.find_element_by_id(EMAIL_FIELD_ID)
        email_field.send_keys(email)

        password_field = self.app.driver.find_element_by_id(PASSWORD_FIELD_ID)
        password_field.send_keys(password)

        submit_btn = self.app.driver.find_element_by_xpath(SUBMIT_BTN_XPATH)
        submit_btn.click()

    def get_logged_in_user_email(self):
        return self.app.driver.find_element_by_xpath(LOGGED_IN_USER_EMAIL_XPATH).text

    def logout(self, email):
        logout_users_cand = self.app.driver.find_elements_by_xpath(USER_EMAIL_XPATH)
        while logout_users_cand:
            cur_el = logout_users_cand.pop()
            if cur_el.text == email:
                logout_user = cur_el
                break
        logout_user.click()
        logout = self.app.driver.find_element_by_xpath(SIGN_OUT_LINK_XPATH)
        logout.click()


