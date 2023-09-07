from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class LoginPage(BaseClass):

    textbox_username = (By.ID, "Email")
    textbox_password = (By.ID, "Password")
    button_Login = (By.XPATH, "//button[text()= 'Log in']")
    button_logout = (By.XPATH, "//a[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.clear_element(*LoginPage.textbox_username)
        self.set_element(LoginPage.textbox_username, username)
        self.clear_element(*LoginPage.textbox_password)
        self.set_element(LoginPage.textbox_password, password)
        self.click_element(*LoginPage.button_Login)





