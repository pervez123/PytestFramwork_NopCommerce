import time

import pytest

from TestData.CustomerRole_TestData import CustomerRoleTestData
from pageObjects.Add_Product import AddProduct
from pageObjects.Product import Products
from utilities.BaseClass import BaseClass


class TestAddProduct(BaseClass):

    @pytest.fixture(params=CustomerRoleTestData.customer_role)
    def getdat(self, request):
        return request.param

    def test_side_menu_link(self):
        self.click_element(*self.catalog_menu_link)
        self.click_element(*self.catalog_submenu_product)

    def test_add_product(self):
        prod_obj = Products(self.driver)
        add_product_obj = prod_obj.click_add_new_btn()
        add_product_obj.add_product("QA Product")
        add_product_obj.sku("SKU001")
        add_product_obj.tinymce_editor("Lorem Ipsum")
        time.sleep(1)
        add_product_obj.select_category("Computers >> Software")
        add_product_obj.manuf_value("HP")
        add_product_obj.product_tags(["camera", "apparel", "tag3"])
        add_product_obj.cust_role("Registered")
        add_product_obj.ltd_to_store("Test store 2")
        add_product_obj.available_start_date()
        time.sleep(1)
        add_product_obj.price(50, 60, 30, 30, "kg(s)")
        add_product_obj.available_for_pre_order("November 2023", "13")
        add_product_obj.require_other_products_checkbox("Apple MacBook Pro 13-inch")
        add_product_obj.downloadable_product("https://docs.python.org/3/library/datetime.html", 20, "Manually",
                                             "C://Users/Mohd Pervez/Downloads/images.jpg")

        add_product_obj.click_element(*self.btn_save)





