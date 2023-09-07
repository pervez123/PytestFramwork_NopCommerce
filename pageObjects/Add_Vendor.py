import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class AddVendor(BaseClass):

    btn_setting_mode = (By.CSS_SELECTOR, ".onoffswitch-label")
    txt_name = (By.ID, "Name")
    txt_tinymce_iframe = (By.CSS_SELECTOR, "#Description_ifr")
    text_body_tinymce = (By.ID, "tinymce")
    txt_email = (By.ID, "Email")
    checkbox_active = (By.ID, "Active")
    file_upload_picture = (By.CSS_SELECTOR, "input[title = 'file input']")
    btn_remove_picture = (By.XPATH, "//span[text() = 'Remove picture']")
    alert_message = (By.XPATH, "//div[contains(@class, 'alert-danger')]")

    def __init__(self, driver):
        self.driver = driver

    def vendor_name(self, name):
        self.clear_element(*AddVendor.txt_name)
        self.set_element(AddVendor.txt_name, name)

    def vendor_tinymce(self, text):
        iframe = self.wait_until_presence_of_element_located(AddVendor.txt_tinymce_iframe)
        self.driver.switch_to.frame(iframe)
        self.set_element(AddVendor.text_body_tinymce, text)
        self.driver.switch_to.default_content()

    def vendor_email(self, email):
        self.clear_element(*AddVendor.txt_email)
        self.set_element(AddVendor.txt_email, email)

    def vendor_profile_pic(self, photo_path):
        self.set_element(AddVendor.file_upload_picture, photo_path)




