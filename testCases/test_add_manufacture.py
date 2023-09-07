import time

import pytest

from pageObjects.Manufacturer import Manufacturer
from pageObjects.Product import Products
from utilities.BaseClass import BaseClass


class TestAddManufacture(BaseClass):

    @pytest.mark.xfail
    def test_menu_link(self):
        self.click_element(*self.catalog_menu_link)
        self.click_element(*self.catalog_manufacturer)

    def test_add_manufacture(self):
        mfg_obj = Manufacturer(self.driver)
        add_mfg_obj = mfg_obj.click_add_new_btn()
        add_mfg_obj.manufacture_name("Samsung")
        add_mfg_obj.click_save_btn()
        assert 'success' in self.success_alert(), "assertion fail"
        time.sleep(1)
        self.click_element(*self.catalog_submenu_product)
        prod_obj = Products(self.driver)
        add_prod_obj = prod_obj.click_add_new_btn()
        self.click_element(*add_prod_obj.manufacture)
        lst_manufacture = self.wait_until_presence_of_all_elements_located(add_prod_obj.lst_manufacture)
        for i in lst_manufacture:
            if i.text != "Samsung":
                continue
            elif i.text == "Samsung":
                assert True
                break




