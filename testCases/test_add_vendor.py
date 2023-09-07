import time
import pytest

from TestData.Vendor_testData import TestData
from pageObjects.Vendor import Vendor
from utilities.BaseClass import BaseClass


class TestAddVendor(BaseClass):

    @pytest.fixture(params=TestData.test_data())
    def getdata(self, request):
        return request.param

    @pytest.mark.xfail
    def test_side_menu(self):
        self.click_on_customer_menu_link()
        self.click_on_vendor_sub_menu_link()

    def test_add_vendor(self, getdata):

        vendor = Vendor(self.driver)
        add_vendor_obj = vendor.click_add_new_btn()
        add_vendor_obj.vendor_name(getdata['Name'])
        add_vendor_obj.vendor_tinymce(getdata['text'])
        # generating random emails
        self.email = self.random_email_generator() + '@gmail.com'
        add_vendor_obj.vendor_email(self.email)
        add_vendor_obj.vendor_profile_pic(getdata['photo_path'])
        time.sleep(8)
        add_vendor_obj.click_save_btn()
        # assert "success" not in self.get_text(*add_vendor_obj.alert_message)
        add_vendor_obj.validation(getdata)

