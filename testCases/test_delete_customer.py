import pytest

from TestData.test_data_customer import CustomerTestData
from pageObjects.Customer import Customer
from pageObjects.Edit_Customer import EditCustomer
from utilities.BaseClass import BaseClass


class TestDeleteCustomer(BaseClass):

    @pytest.fixture(params=CustomerTestData.customer_email)
    def get_email_for_delete(self, request):
        return request.param

    @pytest.mark.xfail
    def test_side_menu(self):
        self.logs().info("-----------Clicking on Customer link from side menu---------------")
        self.click_on_customer_menu_link()
        self.logs().info("-----------Clicking on Customer link from sub menu---------------")
        self.click_on_customer_sub_menu_link()

    def test_delete_customer(self, get_email_for_delete):

        cust = Customer(self.driver)
        abc = cust.click_edit_button_for_specific_email(get_email_for_delete['email'])
        abc.click_element(*EditCustomer.btn_delete_customer)
        abc.click_element(*EditCustomer.btn_popup_delete)
        success_alert = abc.get_alert_success_message()
        assert 'successfully' in success_alert
        self.driver.refresh()
