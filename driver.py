from selenium import webdriver


class Driver(object):
    def __init__(self, browser):
        if browser == "firefox":
            self.driver = webdriver.Firefox("driver/geckodriver.exe")
        elif browser == "remote":
            self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wb/hub')
        else:
            self.driver = webdriver.Chrome("driver/chromedriver.exe")

        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def get(self, url):
        self.driver.get(url)

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def find_elements(self, by, value):
        return self.driver.find_elements(by, value)

    def refresh(self):
        self.driver.refresh()

    def close(self):
        self.driver.close()
