import time

import pytest

from pageObjects.Add_Customer import AddCustomer
from pageObjects.Customer import Customer
from pageObjects.Edit_Customer import EditCustomer
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestEditCustomer(BaseClass):

    def test_edit_customer_details(self):
        self.logs().info("-----------TestCase 03----------------")
        login = LoginPage(self.driver)
        self.logs().info("-----------login with valid credentials---------------")
        login.login("admin@yourstore.com", "admin")
        self.logs().info("-----------login successfully---------------")
        self.logs().info("-----------Clicking on Customer link from side menu---------------")
        self.click_on_customer_menu_link()
        self.logs().info("-----------Clicking on Customer link from sub menu---------------")
        self.click_on_customer_sub_menu_link()
        cust = Customer(self.driver)
        edit_cust = cust.click_edit_button_for_specific_email("qa_02@gmail.com")
        edit_cust.update_email("qa_03@gmail.com")
        edit_cust.update_password("Qa@123009")
        edit_cust.update_first_name('Mr')
        edit_cust.update_lastname("warsi")
        edit_cust.update_gender("M")
        edit_cust.update_dob("12/12/1998")
        edit_cust.update_company_name("Apple")
        edit_cust.update_tax_exempted_checkbox()
        edit_cust.update_manager_of_vendor("Vendor 1")
        edit_cust.update_customer_roles("Vendors")
        edit_cust.click_save_btn()
        success_alert = edit_cust.get_alert_success_message()
        assert "updated successfully" in success_alert

    # @pytest.mark.sanity
    # def test_checkbox(self):
    #     cust = Customer(self.driver)
    #     cust.click_checkbox_for_specific_email("qa_02@gmail.com")
    #     time.sleep(2)
    #     assert self.find_element(*cust.checkbox).is_selected()

    def test_change_password(self):
        cust = Customer(self.driver)
        edit_pass = cust.click_edit_button_for_specific_email("qa_03@gmail.com")
        edit_pass.update_password("A@1345600")
        edit_pass.click_element(*edit_pass.btn_change_password)
        time.sleep(1)
        self.logs().info("---------password updated----------")
        self.logs().info("---------verifying success message---")
        assert edit_pass.get_alert_success_message()
        self.logs().info("---------Entering already used password to update----------")
        edit_pass.update_password("A@1345600")
        edit_pass.click_element(*edit_pass.btn_change_password)
        time.sleep(1)
        self.logs().info("---------verifying error message---")
        assert edit_pass.get_alert_error_message()



