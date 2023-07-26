import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture(scope="module")
def browser(request):
    options = webdriver.FirefoxOptions()
    options.add_argument("-headless")
    _browser = webdriver.Firefox(options=options)
    yield _browser
    _browser.quit()


def test_main_page_loads_and_shows_untitled(browser):
    browser.get("http://localhost:5000")

    # User goes to the homepage of the website
    # She notices the page title
    assert "Notes" in browser.title
    # there is a new document with the title "Untitled"
    inputbox = browser.find_element(By.NAME, "title")
    assert inputbox.get_attribute("placeholder") == "Untitled"

    # The cursor is blinking on the title "Untitled"
    # She types "Buy peacock feathers" as a title
    inputbox.send_keys("Buy peacock feathers")
    # When she hits enter, the page updates, and now the page is redirected to
    # http://localhost:5000/document/1
    # and the title is "Buy peacock feathers"


# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly"
# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep
