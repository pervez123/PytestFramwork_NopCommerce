import time

from selenium.webdriver.common.by import By

from pageObjects.Add_Customer_Role import AddCustomerRole


class EditCustomerRole(AddCustomerRole):

    def update_customer_role_name(self, name):
        self.clear_element(*EditCustomerRole.txt_name)
        self.set_element(EditCustomerRole.txt_name, name)

    def update_customer_checkbox_free_shipping(self):
        self.click_element(*EditCustomerRole.checkbox_free_shipping)

    def update_customer_checkbox_enable_pwd_lifetime(self):
        self.click_element(*EditCustomerRole.checkbox_EnablePwdLifetime)

    def update_customer_checkbox_override_default_tax_display(self):
        self.click_element(*AddCustomerRole.checkbox_override_default_tax_display)

    def update_dropdown_default_tax(self, default_tax_type):
        self.select_by_visible_text(EditCustomerRole.dropdown_DefaultTaxDisplayType, default_tax_type)

    def update_product_name(self, product_name):
        window_before = self.driver.window_handles[0]
        self.click_element(*EditCustomerRole.btn_chooseAProduct)
        time.sleep(3)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        products = self.find_elements(*EditCustomerRole.table_product_list)
        for i in products:
            if i.text == product_name:
                self.logs().info("clicking select button from new window")
                i.find_element(*EditCustomerRole.btn_select).click()
                break

        self.driver.switch_to.window(window_before)
        assert self.get_text(*EditCustomerRole.selected_product_name) == product_name

    def save_btn(self):
        self.click_element(*EditCustomerRole.btn_save)


