import time
import pytest
from TestData.test_data_customer import CustomerTestData
from pageObjects.Add_Customer import AddCustomer
from pageObjects.Customer import Customer
from utilities.BaseClass import BaseClass
from selenium.common import exceptions, NoSuchElementException


class TestAddCustomer(BaseClass):

    @pytest.fixture(params=CustomerTestData.customer_details)
    def dataset(self, request):
        return request.param

    # Its pre-requisite for this specific test case
    @pytest.mark.xfail
    def test_side_menu(self):
        self.logs().info("-----------Clicking on Customer link from side menu---------------")
        self.click_on_customer_menu_link()
        self.logs().info("-----------Clicking on Customer link from sub menu---------------")
        self.click_on_customer_sub_menu_link()

    def test_add_customer(self, dataset):

        self.logs().info(f"----------- TestCase {dataset} - Add Customer ----------------")
        cust = Customer(self.driver)
        add_cust = cust.click_add_btn()
        self.logs().info("-----------Customer details---------------")
        add_cust.set_email(dataset['email'])
        add_cust.set_password(dataset['pass'])
        add_cust.set_firstname(dataset['f_name'])
        add_cust.set_lastname(dataset['l_name'])
        add_cust.select_gender(dataset['gender'])
        add_cust.set_dob(dataset['dob'])
        add_cust.set_company_name(dataset['company_name'])
        add_cust.set_tax_exempted_checkbox()
        time.sleep(3)
        add_cust.set_customer_roles(dataset['customer_role'])
        add_cust.set_manager_of_vendor(dataset['Manager_of_Vendor'])
        add_cust.set_newsletter(dataset['Newsletter'])
        add_cust.click_save_btn()
        self.logs().info("-------------Verifying success message in pop up alert--------------")
        self.validation(dataset, add_cust.link_text_back_to_customer_list)
