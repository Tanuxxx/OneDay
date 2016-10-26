import pytest
from Login.login_page import LoginPage


@pytest.fixture
def login_page():
    fixture = LoginPage()
    return fixture


def test_login_valid_cred(login_page):
    login_page.get()

    email = 'brookdale@mailinator.com'
    password = 'qweqwe'

    login_page.login(email=email, password=password)


def test_verify_page_footer(login_page):
    login_page.get()

    expected_footer_text = 'For support, contact us at support@oneday.com'
    expected_footer_link = 'mailto:support@oneday.com'

    assert (login_page.get_footer_text() == expected_footer_text)
    assert (login_page.get_footer_link() == expected_footer_link)

