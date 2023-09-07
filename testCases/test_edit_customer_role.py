from pageObjects.Customer_Role import CustomerRole
from pageObjects.Edit_Customer_Role import EditCustomerRole
from utilities.BaseClass import BaseClass


class TestEditCustomerRole(BaseClass):

    def test_edit_cust_role(self):
        self.click_on_customer_menu_link()
        self.click_on_customer_roles_sub_menu_link()
        cust_role = CustomerRole(self.driver)
        edit_cust_role = cust_role.click_edit_btn_for_specific_role("Guests")
        self.logs().info("---Updating details----")
        edit_cust_role.update_customer_checkbox_free_shipping()
        edit_cust_role.update_customer_checkbox_enable_pwd_lifetime()
        edit_cust_role.update_dropdown_default_tax('Including tax')
        edit_cust_role.update_product_name('Apple MacBook Pro 13-inch')
        edit_cust_role.save_btn()
        assert 'updated successfully' in self.get_text(*edit_cust_role.alert_message), "Something went wrong"
