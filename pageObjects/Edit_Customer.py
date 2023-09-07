import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass


class EditCustomer(BaseClass):

    table_email_locator = (By.XPATH, "//table//tr/td[2]")
    txt_email = (By.ID, "Email")
    txt_password = (By.NAME, "Password")
    btn_change_password = (By.CSS_SELECTOR, "button[name='changepassword']")
    txt_first_name = (By.ID, "FirstName")
    txt_Last_name = (By.CSS_SELECTOR, "#LastName")
    txt_gender_male = (By.XPATH, "//input[@value = 'M']")
    txt_gender_female = (By.XPATH, "//input[@value = 'F']")
    txt_dob = (By.ID, "DateOfBirth")  # MM/DD/YYYY
    txt_company_name = (By.NAME, "Company")
    checkbox_Is_taxExempted = (By.XPATH, "//input[@class='check-box' and @id='IsTaxExempt']")
    txt_newsletter = (By.XPATH, "//ul[@id = 'SelectedNewsletterSubscriptionStoreIds_taglist']/parent::div") # /parent::div/parent::div")
    newsletter_options = (By.XPATH, "//ul[@id = 'SelectedNewsletterSubscriptionStoreIds_listbox']/li")
    customer_role_field = "//ul[@id='SelectedCustomerRoleIds_taglist']/parent::div/parent::div"
    customer_role_options = "//ul[@id='SelectedCustomerRoleIds_listbox']/li"
    customer_role_registered_delete_icon = "//ul[@id = 'SelectedCustomerRoleIds_taglist']//span[text()='Registered']/"
    "following-sibling::span[@title='delete']"
    customer_role_selected_tags = (By.XPATH, "//ul[@id='SelectedCustomerRoleIds_taglist']/li")
    manager_of_vendor = (By.ID, "VendorId")
    save_btn = (By.NAME, "save")
    alert_success_message = (By.XPATH, "//div[contains(@class, 'alert-success')]")
    alert_error_message = (By.XPATH, "//div[contains(@class, 'alert-danger')]")
    btn_delete_customer = (By.ID, "customer-delete")
    btn_popup_delete = (By.XPATH, "//button[contains(text(),'Delete')]")

    def __init__(self, driver):
        self.driver = driver

    def update_email(self, email):
        self.clear_element(*EditCustomer.txt_email)
        # self.find_element_clear(*EditCustomer.txt_email)
        self.logs().info("---------Enter updated email------------")
        self.set_element(EditCustomer.txt_email, email)
        self.logs().info("---------Email entered--------")

    def update_first_name(self, f_name):
        self.clear_element(*EditCustomer.txt_first_name)
        self.logs().info("---------f_name updated email------------")
        self.set_element(EditCustomer.txt_first_name, f_name)
        self.logs().info("---------updated f_name entered--------")

    def update_password(self, password):
        self.clear_element(*EditCustomer.txt_password)
        # self.find_element_clear(*EditCustomer.txt_password)
        self.logs().info("---------Enter updated password------------")
        self.set_element(EditCustomer.txt_password, password)

    # def change_password_button_click(self):
    #     self.click_element(*EditCustomer.btn_change_password)
        # self.find_element_click(*EditCustomer.btn_change_password)

    def update_lastname(self, l_name):
        self.clear_element(*EditCustomer.txt_Last_name)
        # self.find_element_clear(*EditCustomer.txt_Last_name)
        self.logs().info("---------Updated last name------------")
        self.set_element(EditCustomer.txt_Last_name, l_name)
        # self.find_element_send_keys(*EditCustomer.txt_Last_name, text=l_name)
        self.logs().info("---------last name updated--------- ")

    def update_gender(self, gender):
        self.logs().info("---------selecting gender------------")
        if gender.upper() == 'M' or gender.upper() == "MALE":
            self.click_element(*EditCustomer.txt_gender_male)
            # self.find_element_click(*EditCustomer.txt_gender_male)

        elif gender.upper() == 'F' or gender.upper() == "FEMALE":
            self.click_element(*EditCustomer.txt_gender_female)
            # self.find_element_click(*EditCustomer.txt_gender_female)

        else:
            self.click_element(*EditCustomer.txt_gender_male)
            # self.find_element_click(*EditCustomer.txt_gender_male)

    def update_dob(self, dob):
        self.clear_element(*EditCustomer.txt_dob)
        # self.find_element_clear(*EditCustomer.txt_dob)
        self.logs().info("---------Entering DOB------------")
        self.set_element(EditCustomer.txt_dob, dob)
        # self.find_element_send_keys(*EditCustomer.txt_dob, text=dob)

    def update_company_name(self, company_name):
        self.clear_element(*EditCustomer.txt_company_name)
        # self.find_element_clear(*EditCustomer.txt_company_name)
        self.logs().info("---------Entering company name------------")
        self.set_element(EditCustomer.txt_company_name, company_name)
        # self.find_element_send_keys(*EditCustomer.txt_company_name, text=company_name)

    def update_tax_exempted_checkbox(self):
        self.logs().info("---------un-tick checkbox------------")
        self.click_element(*EditCustomer.checkbox_Is_taxExempted)
        # self.find_element_click(*EditCustomer.checkbox_Is_taxExempted)

    def update_customer_roles(self, customer_role):
        self.click_element(By.XPATH, EditCustomer.customer_role_field)
        # cust_role_field = self.driver.find_element(By.XPATH, EditCustomer.customer_role_field)
        # cust_role_field.click()
        self.logs().info("---------selecting customer role------------")
        if customer_role != 'Guests':
            self.click_element(By.XPATH, EditCustomer.customer_role_options + f"[text()='{customer_role}']")
            # self.find_element_click(By.XPATH, EditCustomer.customer_role_options + f"[text()='{customer_role}']")
        # elif customer_role == 'Registered':
        #     pass
        else:
            try:

                # self.find_element_click(By.XPATH, EditCustomer.customer_role_registered_delete_icon)
                self.click_element(By.XPATH, EditCustomer.customer_role_options + f"[text()='{customer_role}']")
                self.click_element(By.XPATH, EditCustomer.customer_role_registered_delete_icon)
                # self.find_element_click(By.XPATH, EditCustomer.customer_role_options + f"[text()='{customer_role}']")
            except:
                self.click_element(By.XPATH, EditCustomer.customer_role_options + f"[text()='{customer_role}']")
                # self.find_element_click(By.XPATH, EditCustomer.customer_role_options + f"[text()='{customer_role}']")

    def update_manager_of_vendor(self, vendor_name):
        self.logs().info("---------clicking on Manager of vendor field------------")
        # self.driver.find_element(By.ID, "VendorId").click()
        self.click_element(*EditCustomer.manager_of_vendor)
        # self.find_element_click(By.ID, "VendorId")
        self.logs().info("---------selecting the value from dropdown------------")
        self.select_by_visible_text(EditCustomer.manager_of_vendor, vendor_name)

    def update_newsletter(self, store_name):
        # self.driver.find_element(*EditCustomer.txt_newsletter).click()
        self.click_element(*EditCustomer.txt_newsletter)
        # self.find_element_click(*EditCustomer.txt_newsletter)
        # store_options = self.driver.find_elements(*EditCustomer.newsletter_options)
        store_options = self.find_elements(*EditCustomer.newsletter_options)
        for i in store_options:
            if i.text == store_name:
                i.click()
                break

    def click_save_btn(self):
        # self.driver.find_element(*EditCustomer.save_btn).click()
        self.click_element(*EditCustomer.save_btn)
        # self.find_element_click(*EditCustomer.save_btn)

    def get_alert_success_message(self):
        # return self.driver.find_element(*EditCustomer.alert_message).text
        return self.get_text(*EditCustomer.alert_success_message)
        # return self.find_element_get_text(*EditCustomer.alert_message)

    def get_alert_error_message(self):
        # return self.driver.find_element(*EditCustomer.alert_message).text
        return self.get_text(*EditCustomer.alert_error_message)
