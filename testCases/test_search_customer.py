import time

import pytest
from selenium.webdriver.common.by import By

from TestData.test_data_customer import CustomerTestData
from pageObjects.Customer import Customer
from utilities.BaseClass import BaseClass


class TestSearch(BaseClass):

    @pytest.fixture(params=CustomerTestData.customer_email)
    def get_email_data(self, request):
        return request.param

    @pytest.fixture(params=CustomerTestData.customer_f_name)
    def get_f_name_data(self, request):
        return request.param

    @pytest.mark.xfail
    def test_side_menu(self):
        self.logs().info("-----------Clicking on Customer link from side menu---------------")
        self.click_on_customer_menu_link()
        self.logs().info("-----------Clicking on Customer link from sub menu---------------")
        self.click_on_customer_sub_menu_link()

    def test_search_by_email(self, get_email_data):

        cust = Customer(self.driver)
        self.logs().info(f"----search by {get_email_data['email']}----")
        cust.search_by_email(get_email_data['email'])

        self.driver.refresh()

    def test_search_by_name(self, get_f_name_data):
        cust = Customer(self.driver)
        self.logs().info(f"--------search by {get_f_name_data['f_name']}---------")
        cust.search_by_first_name(get_f_name_data['f_name'])
        self.driver.refresh()


