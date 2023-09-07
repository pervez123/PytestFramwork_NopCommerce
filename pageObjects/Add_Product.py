import time
from datetime import datetime

from selenium.common import NoSuchElementException, exceptions, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class AddProduct(BaseClass):

    txt_product_name = (By.ID, "Name")
    txt_short_description = (By.ID, "ShortDescription")
    tinymce_iframe = (By.ID, "FullDescription_ifr")
    tinymce_body = (By.ID, "tinymce")
    txt_sku = (By.ID, "Sku")
    category = (By.XPATH, "//ul[@id = 'SelectedCategoryIds_taglist']/parent::div")
    lst_category = (By.XPATH, "//ul[@id = 'SelectedCategoryIds_listbox']/li")
    manufacture = (By.XPATH, "//ul[@id = 'SelectedManufacturerIds_taglist']/parent::div")
    lst_manufacture = (By.XPATH, "//ul[@id = 'SelectedManufacturerIds_listbox']/li")
    txt_product_tag = (By.XPATH, "//ul[@class='tag-editor ui-sortable']")
    dropdown_product_type = (By.ID, "ProductTypeId")
    customer_role = (By.XPATH, "//ul[@id = 'SelectedCustomerRoleIds_taglist']/parent::div")
    customer_role_lst = (By.XPATH, "//ul[@id = 'SelectedCustomerRoleIds_listbox']/li")
    limited_to_store = (By.XPATH, "//ul[@id = 'SelectedStoreIds_taglist']/parent::div")
    limited_to_store_lst = (By.XPATH, "//ul[@id = 'SelectedStoreIds_listbox']/li")
    checkbox_RequireOtherProducts = (By.NAME, "RequireOtherProducts")
    btn_btnAddNewRequiredProduct = (By.ID, "btnAddNewRequiredProduct")
    selected_product_name = (By.ID, "required-product-names")
    tag_list = (By.XPATH, "//li[@class = 'ui-menu-item']/div]")
    txt_AvailableStartDate = (By.ID, "AvailableStartDateTimeUtc")
    MarkAsNew = (By.ID, "MarkAsNew")
    MarkAsNewStartDateTimeUtc = (By.NAME, "MarkAsNewStartDateTimeUtc")
    title_price = (By.XPATH, "//div[@class = 'card-title' and text() = 'Prices']")
    expand_product_price = (By.XPATH, "//div[@class = 'card card-secondary card-outline collapsed-card' and "
                                      "@id='product-price']//button[@data-card-widget='collapse']")
    txt_price = (By.XPATH, "//div[@id='product-price-area']//input[1]")
    txt_old_price = (By.XPATH, "//input[@id = 'OldPrice']/preceding-sibling::input")
    checkbox_BasePriceEnabled = (By.ID, "BasepriceEnabled")
    txt_BasePriceAmount = (By.XPATH, "//input[@id = 'BasepriceAmount']/preceding-sibling::input")
    dropdown_BasePriceUnitProduct = (By.ID, "BasepriceUnitId")
    checkbox_IsTelecommunicationsOrBroadcastingOrElectronicServices = (By.NAME, "IsTelecommunicationsOrBroadcasting"
                                                                                "OrElectronicServices")
    table_product_list = (By.XPATH, "//table//tr//td[2]")
    btn_select = (By.XPATH, "preceding-sibling::td")
    calender_current_month_year = "//a[@aria-live='assertive']"
    calender_next_icon = "//a[@aria-label='Next']"
    calender_current_month_date = "//table[@class = 'k-content k-month']//tr//td[not (contains(@class, 'k-other-month'))]"
    checkbox_available_pre_order = (By.ID, "AvailableForPreOrder")
    calender_date_view_available_pre_order = (By.XPATH, "//span[@aria-controls='"
                                                        "PreOrderAvailabilityStartDateTimeUtc_dateview']")
    btn_expand_download_product = (By.XPATH, "//div[contains(@class, 'collapsed-card') and @id = 'product-downloadable'"
                                             "]//button[@data-card-widget='collapse']")
    checkbox_downloadable_product = (By.ID, "IsDownload")
    checkbox_DownloadFile_UseDownloadUrl = (By.XPATH, "//div[@id = 'pnlDownloadFile']//input[contains"
                                                      "(@id,'UseDownloadURL')]")
    txt_DownloadFile_DownloadUrl = (By.XPATH, "//div[@id = 'pnlDownloadFile']//input[contains(@id,'downloadurl')]")
    btn_DownloadFile_SaveDownloadBtn = (By.XPATH, "//div[@id = 'pnlDownloadFile']//button"
                                                  "[contains(@id,'saveDownloadUrl')]")
    checkbox_unlimitedDownloads = (By.ID, "UnlimitedDownloads")
    txt_MaxNumberOfDownloads = (By.XPATH, "//input[@id = 'MaxNumberOfDownloads']")  # /preceding-sibling::input")
    checkbox_HasSampleDownloadFiles = (By.ID, "HasSampleDownload")
    file_upload_SampleDownloadFile = (By.XPATH, "//div[@id = 'pnlSampleDownloadFile']//input[@title = 'file input']")
    dropdown_DownloadActivationTypeId = (By.ID, "DownloadActivationTypeId")

    def __init__(self, driver):
        self.driver = driver

    def add_product(self, name):
        self.clear_element(*AddProduct.txt_product_name)
        self.set_element(AddProduct.txt_product_name, name)

    def tinymce_editor(self, tinymce_text):
        # iframe = self.find_element(*AddProduct.tinymce_iframe)
        iframe = self.wait_until_presence_of_element_located(AddProduct.tinymce_iframe)
        self.driver.switch_to.frame(iframe)
        time.sleep(1)
        self.set_element(AddProduct.tinymce_body, tinymce_text)
        self.driver.switch_to.default_content()

    def sku(self, sku):
        self.set_element(AddProduct.txt_sku, sku)

    def select_category(self, category_value):
        self.select_value_from_static_list(AddProduct.category, AddProduct.lst_category, category_value)

    def manuf_value(self, manufacture_value):
        self.select_value_from_static_list(AddProduct.manufacture, AddProduct.lst_manufacture, manufacture_value)

    def cust_role(self, customer_role):
        self.select_value_from_static_list(AddProduct.customer_role, AddProduct.customer_role_lst, customer_role)

    def ltd_to_store(self, store_name):
        self.select_value_from_static_list(AddProduct.limited_to_store, AddProduct.limited_to_store_lst, store_name)

    def require_other_products_checkbox(self, product_name):
        self.click_element(*AddProduct.checkbox_RequireOtherProducts)
        window_before = self.driver.window_handles[0]
        self.click_element(*AddProduct.btn_btnAddNewRequiredProduct)
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
        products = self.wait_until_presence_of_all_elements_located(AddProduct.table_product_list)
        for i in products:
            if i.text == product_name:
                # self.logs().info("clicking select button from new window")
                i.find_element(*AddProduct.btn_select).click()
                break
        self.driver.switch_to.window(window_before)
        assert self.wait_for_text(AddProduct.selected_product_name, product_name)

    # Tag Editor
    def product_tags(self, tags_to_add):
        for tag in tags_to_add:
            self.driver.execute_script(
                f'$("#ProductTags").tagEditor("addTag", "{tag}");'
            )
            time.sleep(1)

    def available_start_date(self):
        date_time = datetime.now()
        self.set_element(AddProduct.txt_AvailableStartDate, date_time.strftime("%m/%d/%Y %I:%M %p"))

    def price(self, price, old_price, product_cost, base_price, unit_product_value):
        try:
            self.set_element(AddProduct.txt_price, price)
            self.scroll_to_element(AddProduct.title_price)
        except ElementNotInteractableException:
            self.click_element(*AddProduct.expand_product_price)
            self.set_element(AddProduct.txt_price, price)
        self.action_method().send_keys(Keys.TAB).perform()
        self.action_method().send_keys(old_price).perform()
        self.action_method().send_keys(Keys.DELETE).perform()
        self.action_method().send_keys(Keys.TAB).perform()
        self.action_method().send_keys(product_cost).perform()
        self.action_method().send_keys(Keys.DELETE).perform()
        self.click_element(*AddProduct.checkbox_BasePriceEnabled)
        self.action_method().send_keys(Keys.TAB).perform()
        self.action_method().send_keys(Keys.DELETE).perform()
        self.action_method().send_keys(base_price).perform()
        self.action_method().send_keys(Keys.TAB)
        self.select_by_visible_text(AddProduct.dropdown_BasePriceUnitProduct, unit_product_value)
        self.action_method().send_keys(Keys.TAB).perform()

    def available_for_pre_order(self, travel_month_year, travel_date):
        self.click_element(*AddProduct.checkbox_available_pre_order)
        self.click_element(*AddProduct.calender_date_view_available_pre_order)
        time.sleep(1)
        self.calender((By.XPATH, AddProduct.calender_current_month_year), (By.XPATH, AddProduct.calender_next_icon),
                      (By.XPATH, AddProduct.calender_current_month_date), travel_month_year, travel_date)

    def downloadable_product(self, url, max_download, txt, file_url):
        try:
            self.click_element(*AddProduct.checkbox_downloadable_product)
        except ElementNotInteractableException:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click_element(*AddProduct.btn_expand_download_product)
            self.click_element(*AddProduct.checkbox_downloadable_product)
        use_download_url = self.wait_until_presence_of_element_located(AddProduct.checkbox_DownloadFile_UseDownloadUrl)
        use_download_url.click()
        self.set_element(AddProduct.txt_DownloadFile_DownloadUrl, url)
        self.click_element(*AddProduct.btn_DownloadFile_SaveDownloadBtn)
        unlimited_download_status = self.find_element(*AddProduct.checkbox_unlimitedDownloads)
        if unlimited_download_status.is_selected():
            self.click_element(*AddProduct.checkbox_unlimitedDownloads)
        else:
            pass
        # input_field = self.wait_until_element_to_be_clickable(AddProduct.txt_MaxNumberOfDownloads)
        # input_field.clear()
        self.action_method().send_keys(Keys.TAB).perform()
        self.action_method().key_down(Keys.CONTROL).send_keys('A').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        self.action_method().send_keys(max_download)
        # self.driver.execute_script("arguments[0].value = '';", input_field)
        # self.set_element(AddProduct.txt_MaxNumberOfDownloads, max_download)
        time.sleep(1)
        # self.action_method().send_keys(*max_download)
        # self.set_element(AddProduct.txt_MaxNumberOfDownloads, max_download)
        self.select_by_visible_text(AddProduct.dropdown_DownloadActivationTypeId, txt)
        self.click_element(*AddProduct.checkbox_HasSampleDownloadFiles)
        file_upload = self.wait_until_presence_of_element_located(AddProduct.file_upload_SampleDownloadFile)
        file_upload.send_keys(file_url)
        time.sleep(1)




