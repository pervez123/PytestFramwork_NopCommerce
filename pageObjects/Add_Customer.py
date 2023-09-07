import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utilities.BaseClass import BaseClass


class AddCustomer(BaseClass):

    txt_email = (By.ID, "Email")
    txt_password = (By.NAME, "Password")
    txt_first_name = (By.CSS_SELECTOR, "#FirstName")
    txt_Last_name = (By.CSS_SELECTOR, "#LastName")
    txt_gender_male = (By.XPATH, "//input[@value = 'M']")
    txt_gender_female = (By.XPATH, "//input[@value = 'F']")
    txt_dob = (By.ID, "DateOfBirth")  # MM/DD/YYYY
    txt_company_name = (By.NAME, "Company")
    checkbox_Is_taxExempted = (By.XPATH, "//input[@class='check-box' and @id='IsTaxExempt']")
    txt_newsletter = (By.XPATH, "//ul[@id = 'SelectedNewsletterSubscriptionStoreIds_taglist']/parent::div") # /parent::div/parent::div")
    newsletter_options = (By.XPATH, "//ul[@id = 'SelectedNewsletterSubscriptionStoreIds_listbox']/li")
    customer_role_field = (By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/parent::div/parent::div")
    customer_role_options = "//ul[@id='SelectedCustomerRoleIds_listbox']/li"
    customer_role_registered_delete_icon = "//ul[@id = 'SelectedCustomerRoleIds_taglist']//span[text()='Registered']/"\
                                           "following-sibling::span[@title='delete']"
    manager_of_vendor = (By.ID, "VendorId")
    save_btn = (By.NAME, "save")
    link_text_back_to_customer_list = (By.LINK_TEXT, "back to customer list")
    alert_message = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    alert_error = (By.CSS_SELECTOR, ".alert-danger")
    validation_error = (By.XPATH, "//div[@class = 'validation-summary-errors']//li")

    def __init__(self, driver):
        self.driver = driver

    # def click_on_add_new_button(self):
    #     self.click_element(*self.btn_add_new)
    #     # self.click_element(*AddCustomer.btn_add_new)

    def set_email(self, email):
        self.set_element(AddCustomer.txt_email, email)

    def set_password(self, password):
        self.logs().info("---------Entering password------------")
        self.set_element(AddCustomer.txt_password, password)

    def set_firstname(self, f_name):
        self.logs().info("---------Entering first name------------")
        self.set_element(AddCustomer.txt_first_name, f_name)

    def set_lastname(self, l_name):
        self.logs().info("---------Entering last name------------")
        self.set_element(AddCustomer.txt_Last_name, l_name)

    def select_gender(self, gender):
        self.logs().info("---------selecting gender------------")
        if gender.upper() == 'M' or gender.upper() == "MALE":
            self.click_element(*AddCustomer.txt_gender_male)
        elif gender.upper() == 'F' or gender.upper() == "FEMALE":
            self.click_element(*AddCustomer.txt_gender_female)
        else:
            self.click_element(*AddCustomer.txt_gender_male)

    def set_dob(self, dob):
        self.logs().info("---------Entering DOB------------")
        self.set_element(AddCustomer.txt_dob, dob)

    def set_company_name(self, company_name):
        self.logs().info("---------Entering company name------------")
        self.set_element(AddCustomer.txt_company_name, company_name)

    def set_tax_exempted_checkbox(self):
        self.logs().info("---------clicking checkbox------------")
        self.click_element(*AddCustomer.checkbox_Is_taxExempted)

    def set_customer_roles(self, customer_role):
        self.click_element(*AddCustomer.customer_role_field)
        time.sleep(1)
        self.logs().info("---------selecting customer role------------")
        if customer_role != 'Guests':
            self.click_element(By.XPATH, AddCustomer.customer_role_options + f"[text()='{customer_role}']")
        elif customer_role == 'Registered':
            pass
        else:
            try:
                self.click_element(By.XPATH, AddCustomer.customer_role_options + f"[text()='{customer_role}']")
                self.click_element(By.XPATH, AddCustomer.customer_role_registered_delete_icon)

            except NoSuchElementException:
                self.click_element(By.XPATH, AddCustomer.customer_role_options + f"[text()='{customer_role}']")

    def set_manager_of_vendor(self, vendor_name):
        self.logs().info("---------clicking on Manager of vendor field------------")
        self.click_element(By.ID, "VendorId")
        self.logs().info("---------selecting the value from dropdown------------")
        self.select_by_visible_text(AddCustomer.manager_of_vendor, vendor_name)

    def set_newsletter(self, store_name):
        self.click_element(*AddCustomer.txt_newsletter)
        store_options = self.find_elements(*AddCustomer.newsletter_options)
        for i in store_options:
            if i.text == store_name:
                i.click()
                break

    def click_save_btn(self):
        self.click_element(*AddCustomer.save_btn)

    def back_to_customer_list(self):
        self.click_element(*AddCustomer.link_text_back_to_customer_list)

    def success_popup(self):
        return self.find_element(*AddCustomer.alert_message)

    def success_popup_text(self):
        return self.get_text(*AddCustomer.alert_message)

    def error_popup(self):
        return self.find_element(*AddCustomer.alert_error)

    def error_popup_text(self):
        return self.get_text(*AddCustomer.alert_error)

    def validation_error_msg(self):
        return self.find_element(*AddCustomer.validation_error)

    def validation_error_msg_text(self):
        return self.get_text(*AddCustomer.validation_error)