from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL="https://orteil.dashnet.org/cookieclicker/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

# sleep while page loads
time.sleep(10)

# select the language (English)
language_button_eng = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
language_button_eng.click()

# sleep while page loads
time.sleep(10)

cookie = driver.find_element(By.XPATH, value='//*[@id="bigCookie"]')
available_addons = driver.find_elements(By.CLASS_NAME, value='enabled')

while True:
    # click button for 5 seconds
    start_time = time.time()
    while time.time() - start_time < 5:
        cookie.click()
    available_addons = driver.find_elements(By.CLASS_NAME, value='enabled')
    available_addons[len(available_addons) - 1].click()
