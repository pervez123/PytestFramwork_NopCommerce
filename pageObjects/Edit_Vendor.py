from pageObjects.Add_Vendor import AddVendor


class EditVendor(AddVendor):

    def edit_vendor_name(self, name):
        self.clear_element(*EditVendor.txt_name)
        self.set_element(EditVendor.txt_name, name)

    def edit_tinymce_description(self, text):
        iframe = self.find_element(*EditVendor.txt_tinymce_iframe)
        self.driver.switch_to.frame(iframe)
        self.set_element(EditVendor.txt_tinymce_iframe, text)

    def update_profile_pic(self, photo_path):
        self.set_element(EditVendor.file_upload_picture, photo_path)

    def click_save(self):
        self.click_element(*EditVendor.btn_save)
