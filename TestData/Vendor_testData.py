from utilities.BaseClass import BaseClass


class TestData(BaseClass):

    @staticmethod
    def test_data():
        return TestData.excel_test_data("C:\\Users\\Mohd Pervez\\Downloads\\AutomationTestData.xlsx", "vendor")
