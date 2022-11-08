from selenium import webdriver
from selenium.webdriver.common.by import By
import time
# Open Browser
browser = webdriver.Chrome()

# Got to webpage
browser.get("https://practicetestautomation.com/practice-test-login/")

# Type username student into Username field
username_locator = browser.find_element(By.ID, "username")
username_locator.send_keys("student")
# Type password Password123 into Password field
password_locator = browser.find_element(By.NAME, "password")
password_locator.send_keys("Password123")
# Push Submit button
submit_button = browser.find_element(By.XPATH, "//button[@class='btn']")
submit_button.click()
# This should be changed to a selenium wait, but following course guide
time.sleep(2)

# Verify new page URL contains practicetestautomation.com/logged-in-successfully/
actual_url = browser.current_url
assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"
# Verify new page contains expected text ('Congratulations' or 'successfully logged in')
text_locator = browser.find_element(By.TAG_NAME, "h1")
actual_text = text_locator.text
assert actual_text == "Logged In Successfully"

# Verify button Log out is displayed on the new page
log_out_button_locator = browser.find_element(By.LINK_TEXT, "Log out")
assert log_out_button_locator.is_displayed()
browser.close()
