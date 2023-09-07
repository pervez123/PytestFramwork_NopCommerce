from selenium.webdriver.common.by import By

from pageObjects.Add_Manufacture import AddManufacture
from utilities.BaseClass import BaseClass


class Manufacturer(BaseClass):

    btn_add_new = (By.XPATH, "//a[@href='/Admin/Manufacturer/Create']")

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_btn(self):
        self.click_element(*Manufacturer.btn_add_new)
        add_menu_obj = AddManufacture(self.driver)
        return add_menu_obj
