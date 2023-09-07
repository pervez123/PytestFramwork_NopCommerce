from datetime import datetime
import time
import pytest
from TestData.test_data_login import LoginTestData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    @pytest.fixture(params=LoginTestData.login_credentials)
    def dataset(self, request):
        return request.param

    def test_homepage(self):
        self.logs().info("-----------TestCase 01----------------")
        self.logs().info("-----------Verifying Title of the page---------------")
        assert self.driver.title == "Your store. Login", self.logs().error(self.driver.save_screenshot(".\\Screenshots\\abc.png"))

    def test_login(self, dataset):
        self.logs().info("-----------TestCase 02----------------")
        login = LoginPage(self.driver)
        login.login(dataset['user_name'], dataset['password'])
        self.logs().info(f"-----------User_name = {dataset['user_name']}, Password = {dataset['password']}------------")
        lst = []
        act_title = self.driver.title
        exp_title = "Dashboard / nopCommerce administration"

        if act_title == exp_title:
            if dataset['expected_result'] == "pass":
                lst.append("pass")
                self.logs().info("******* Login test Pass ********")
                self.click_element(*login.button_logout)
            elif dataset['expected_result'] == "fail":
                lst.append("fail")
                self.logs().error("******* Login test fail ********")
                self.click_element(*login.button_logout)

        elif act_title != exp_title:
            if dataset['expected_result'] == "pass":
                lst.append("fail")
                self.logs().error("******* Login test fail ********")

            elif dataset['expected_result'] == "fail":
                lst.append("pass")
                self.logs().info("******* Login test pass ********")

        if "fail" in lst:
            self.logs().error("********* Some of the combination failed ***********")
            assert False

        else:
            assert True
