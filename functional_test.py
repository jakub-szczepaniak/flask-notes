import time

from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument("-headless")
browser = webdriver.Firefox(options=options)

browser.get("http://localhost:5000")

# User goes to the homepage of the website
#
# browser.get("http://localhost:8000")

# She notices the page title
assert "Notes" in browser.title
# there is a new document with the title "Untitled"
assert "Untitled" in browser.page_source
# the document has optional title
# the document has either "root" as a parent or valid document id as a parent
# the document has a unique id
# the document can have children


# The cursor is blinking on the title "Untitled"

# She types "Buy peacock feathers" as a title

# When she hits enter, the page updates, and now the page is redirected to
# http://localhost:8000/document/1
# and the title is "Buy peacock feathers"
#
# There is still a text box inviting her to add another item. She
# enters "Use peacock feathers to make a fly"
# The page updates again, and now shows both items on her list

# Edith wonders whether the site will remember her list. Then she sees
# that the site has generated a unique URL for her -- there is some
# explanatory text to that effect.

# She visits that URL - her to-do list is still there.

# Satisfied, she goes back to sleep

browser.quit()
