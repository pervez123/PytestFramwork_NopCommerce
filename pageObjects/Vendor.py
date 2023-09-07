from selenium.webdriver.common.by import By

from pageObjects.Add_Vendor import AddVendor
from pageObjects.Edit_Vendor import EditVendor
from utilities.BaseClass import BaseClass


class Vendor(BaseClass):

    btn_add_new = (By.XPATH, "//a[@href='/Admin/Vendor/Create']")
    txt_vendor_name = (By.ID, "SearchName")
    txt_vendor_email = (By.ID, "SearchEmail")
    btn_search = (By.ID, "search-vendors")
    table_column = "//table//tr/td"
    btn_edit = (By.XPATH, "following-sibling::td[3]/a")

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_btn(self):
        self.click_element(*Vendor.btn_add_new)
        add_vendor = AddVendor(self.driver)
        return add_vendor

    def click_edit_btn_for_specific_vendor(self, vendor_name):
        vendors = self.find_elements(By.XPATH, Vendor.table_column + '[1]')
        for i in vendors:
            if i.text == vendor_name:
                i.click_element(*Vendor.btn_edit)
                break
        edit_vendor = EditVendor(self.driver)
        return edit_vendor
