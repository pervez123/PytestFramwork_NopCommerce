from pageObjects.Add_Customer_Role import AddCustomerRole
from pageObjects.Edit_Customer_Role import EditCustomerRole
from utilities.BaseClass import BaseClass
from selenium.webdriver.common.by import By


class CustomerRole(BaseClass):

    btn_add_new = (By.XPATH, "//a[@href='/Admin/CustomerRole/Create']")
    table_column = "//table//tr//td"
    btn_edit = (By.XPATH, 'following-sibling::td[5]/a')

    def __init__(self, driver):
        self.driver = driver

    def click_add_btn(self):
        self.click_element(*CustomerRole.btn_add_new)
        add_cust_role = AddCustomerRole(self.driver)
        return add_cust_role

    def click_edit_btn_for_specific_role(self, role):
        customer_roles = self.find_elements(By.XPATH, CustomerRole.table_column + '[1]')
        for i in customer_roles:
            if i.text == role:
                i.find_element(*CustomerRole.btn_edit).click()
                break
        edit_cust_role = EditCustomerRole(self.driver)
        return edit_cust_role




