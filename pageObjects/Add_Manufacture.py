from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class AddManufacture(BaseClass):

    txt_name = (By.ID, "Name")

    def __init__(self, driver):
        self.driver = driver

    def manufacture_name(self, name):
        self.set_element(AddManufacture.txt_name, name)

