from selenium.webdriver.common.by import By

from pageObjects.Add_Product import AddProduct
from utilities.BaseClass import BaseClass


class Products(BaseClass):

    btn_add_new = (By.XPATH, "//a[@href='/Admin/Product/Create']")
    table = "//table//tr//td"
    btn_edit = (By.XPATH, "following-sibling::td[5]")

    def __init__(self, driver):
        self.driver = driver

    def click_add_new_btn(self):
        self.click_element(*Products.btn_add_new)
        add_product_obj = AddProduct(self.driver)
        return add_product_obj

