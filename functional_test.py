import time

from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("-headless")
browser = webdriver.Firefox(options=options)

browser.get("http://localhost:5000")


assert "localhost" in browser.current_url
