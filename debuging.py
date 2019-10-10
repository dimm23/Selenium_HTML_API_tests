import unittest
import selenium
from selenium import webdriver
import page

class MyTestResult(unittest.TestResult):
    def addFailure(self, test, err):
        #print(str(test) + ": " + str(err))
        test_name = str(test).split(" ")[0]
        print(str(test_name) + ": Failed")
        super(MyTestResult, self).addFailure(test, err)

    def addError(self, test, err):
        test_name = str(test).split(" ")[0]
        print(str(test_name) + ": " + str(err[1]))
        super(MyTestResult, self).addError(test, err)
        
class DebugingTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("driver/chromedriver.exe")
        #self.driver.maximize_window()
        self.driver.implicitly_wait(10)        
        self.driver.get("http://127.0.0.1:"+page.settings.apiPort+"/api/help") # /api/help
        #self.driver.get("http://127.0.0.1:"+page.settings.apiPort)              # node.js
        self.main_page = page.MainPage(self.driver)

    def test_sendInstantInvitation(self):
        self.main_page.sendInstantInvitation()

    def tearDown(self):
        self.main_page.enter_access_token()
        self.main_page.execute()
        assert self.main_page.no_errors_in_response(), "There is Error in Response"
        #self.driver.close()
            
if __name__ == "__main__":
    unittest.main(testRunner=unittest.TextTestRunner(resultclass=MyTestResult))    
    #unittest.main()