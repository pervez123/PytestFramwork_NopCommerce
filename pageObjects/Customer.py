import time

from selenium.webdriver.common.by import By

from pageObjects.Add_Customer import AddCustomer
from pageObjects.Edit_Customer import EditCustomer
from utilities.BaseClass import BaseClass


class Customer(BaseClass):

    email_field = (By.CSS_SELECTOR, "#SearchEmail")
    first_name = (By.CSS_SELECTOR, "#SearchFirstName")
    last_name = (By.CSS_SELECTOR, "#SearchLastName")
    search_btn = (By.CSS_SELECTOR, "#search-customers")
    btn_add_new = (By.XPATH, "//a[@href='/Admin/Customer/Create']")
    table_column = "//table//tr/td"
    tbl_edit_email = (By.XPATH, "following-sibling::td/a[contains(@href, 'Edit')]")
    tbl_checkbox_email = (By.XPATH, "preceding-sibling::td/input[@type='checkbox']")
    checkbox = (By.XPATH, table_column + "/preceding-sibling::td/input[@type='checkbox']")

    def __init__(self, driver):
        self.driver = driver

    def click_add_btn(self):
        self.click_element(*Customer.btn_add_new)
        add_cust = AddCustomer(self.driver)
        return add_cust

    def click_edit_button_for_specific_email(self, email):
        table_email_list = self.wait_until_presence_of_all_elements_located((By.XPATH, Customer.table_column + '[2]'))
        for i in table_email_list:
            if i.text == email:
                i.find_element(*Customer.tbl_edit_email).click()
                break
        edit_cust = EditCustomer(self.driver)
        return edit_cust

    def click_checkbox_for_specific_email(self, email):
        table_email_list = self.wait_until_presence_of_all_elements_located((By.XPATH, Customer.table_column + '[2]'))
        for i in table_email_list:
            if i.text == email:
                i.find_element(*Customer.tbl_checkbox_email).click()
                break

    def search_by_email(self, email):
        self.clear_element(*Customer.email_field)
        self.set_element(Customer.email_field, email)
        self.click_element(*Customer.search_btn)
        self.clear_element(*Customer.email_field)
        time.sleep(2)
        searched_email = self.wait_for_text((By.XPATH, Customer.table_column + '[2]'),
                                            text=email)
        assert searched_email, self.logs().info("-------Test fail--------")

    def search_by_first_name(self, f_name):
        self.clear_element(*Customer.first_name)
        self.set_element(Customer.first_name, f_name)
        self.click_element(*Customer.search_btn)
        time.sleep(2)
        searched_name_result = self.wait_until_presence_of_all_elements_located(
            (By.XPATH, Customer.table_column + '[3]'))
        for i in searched_name_result:
            assert f_name in i.text



