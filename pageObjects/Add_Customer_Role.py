import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class AddCustomerRole(BaseClass):

    txt_name = (By.CSS_SELECTOR, "#Name")
    checkbox_active = (By.CSS_SELECTOR, "#Active")
    checkbox_free_shipping = (By.CSS_SELECTOR, "#FreeShipping")
    checkbox_tax_exempt = (By.CSS_SELECTOR, "#TaxExempt")
    checkbox_override_default_tax_display = (By.CSS_SELECTOR, "#OverrideTaxDisplayType")
    dropdown_DefaultTaxDisplayType = (By.ID, "DefaultTaxDisplayTypeId")
    checkbox_EnablePwdLifetime = (By.NAME, "EnablePasswordLifetime")
    btn_chooseAProduct = (By.XPATH, "//button[contains(text(), 'Choose a product')]")
    selected_product_name = (By.XPATH, "//span[@id='purchased-with-product-name']")
    txt_system_info = (By.CSS_SELECTOR, "#SystemName")
    table_product_name_list = (By.XPATH, "//table//tr//td[2]")
    btn_select = (By.XPATH, "preceding-sibling::td")
    link_product_pagination = (By.XPATH, "//ul[@class = 'pagination']/li[not (contains(@class,'next') or "
                                         "contains(@class, 'previous'))]")
    link_pagination_next = (By.XPATH, "//ul[@class = 'pagination']/li[contains(@class,'next')]")
    btn_save = (By.NAME, "save")
    alert_message = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    field_validation_error = (By.CSS_SELECTOR, ".field-validation-error")
    link_text_back_to_customer_role_list = (By.LINK_TEXT, "back to customer role list")

    def __init__(self, driver):
        self.driver = driver

    def add_customer_role(self, name, default_tax_type, product_name):
        self.clear_element(*AddCustomerRole.txt_name)
        self.set_element(AddCustomerRole.txt_name, name)
        self.click_element(*AddCustomerRole.checkbox_active)
        self.click_element(*AddCustomerRole.checkbox_override_default_tax_display)
        self.select_by_visible_text(AddCustomerRole.dropdown_DefaultTaxDisplayType, default_tax_type)
        window_before = self.driver.window_handles[0]
        self.click_element(*AddCustomerRole.btn_chooseAProduct)
        time.sleep(3)
        window_after = self.driver.window_handles[1]
        self.logs().info("----Switching to new window--")
        self.driver.switch_to.window(window_after)
        pagination = self.find_elements(*AddCustomerRole.link_product_pagination)
        for page in range(len(pagination)):
            products = self.find_elements(*AddCustomerRole.table_product_name_list)
            for i in products:
                if i.text != product_name:
                    continue
                else:
                    self.logs().info("clicking select button from new window")
                    i.find_element(*AddCustomerRole.btn_select).click()
                    break

            else:
                self.click_element(*AddCustomerRole.link_pagination_next)
                time.sleep(2)
                continue

            break

        self.driver.switch_to.window(window_before)
        assert self.get_text(*AddCustomerRole.selected_product_name) == product_name
        time.sleep(2)
        self.click_save_btn()

