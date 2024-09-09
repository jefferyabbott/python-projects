from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL="https://orteil.dashnet.org/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# sleep while page loads
time.sleep(5)

# select the language (English)
language_button_eng = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
language_button_eng.click()

# sleep while page loads
time.sleep(5)

cookie = driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')
available_addons = driver.find_elements(By.CLASS_NAME, value='enabled')
last_purchased_index = -1

while True:
    # click button for 5 seconds and then check what's available to purchase
    start_time = time.time()
    while time.time() - start_time < 5:
        cookie.click()
    available_addons = driver.find_elements(By.CLASS_NAME, value='enabled')
    if len(available_addons) -1 > last_purchased_index:
        available_addons[len(available_addons) - 1].click()
        last_purchased_index = len(available_addons) - 1
