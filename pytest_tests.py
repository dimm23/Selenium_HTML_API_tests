import pytest
import selenium
from selenium import webdriver
import page


@pytest.fixture
def selenium(selenium):
    selenium.implicitly_wait(10)
    selenium.maximize_window()
    return selenium

@pytest.fixture
def chrome_options(chrome_options):
    chrome_options.binary_location = "driver/chromedriver.exe"
    #chrome_options.add_extension('/path/to/extension.crx')
    chrome_options.add_argument('--kiosk')
    return chrome_options




def test_sendChannelPicture(selenium):
    print("test is started")
    selenium.get("127.0.0.1:20008/api/help")
    page.sendChannelPicture()

