
import pytest
from TestData.CustomerRole_TestData import CustomerRoleTestData
from pageObjects.Customer_Role import CustomerRole
from utilities.BaseClass import BaseClass


class TestAddCustomerRole(BaseClass):

    @pytest.fixture(params=CustomerRoleTestData.customer_role)
    def dataset(self, request):
        return request.param

    @pytest.mark.xfail
    def test_pre_requisite(self):
        self.click_on_customer_menu_link()
        self.click_on_customer_roles_sub_menu_link()

    def test_add_customer_role(self, dataset):
        cust_role = CustomerRole(self.driver)
        add_customer_role = cust_role.click_add_btn()
        self.logs().info("-----Adding Customer Role-------")
        add_customer_role.add_customer_role(dataset['Name'], dataset['default_tax_type'], dataset['Product_name'])
        self.validation(dataset, add_customer_role.link_text_back_to_customer_role_list)
