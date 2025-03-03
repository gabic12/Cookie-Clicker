from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
import random

#Setting up Selenium driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

#List od upgrade IDs
upgrade_id = ["buyCursor", "buyGrandma", "buyFactory", "buyMine", "buyShipment", "buyAlchemy lab", "buyPortal", "buyTime machine"]

#Cookie button
cookie = driver.find_element(By.ID, "cookie")

while True:
    cookie.click()

    random_upgrade = random.choice(upgrade_id)
    upgrade_button = driver.find_element(By.ID, random_upgrade)
    try:
        upgrade_button.click()
    except StaleElementReferenceException: #Because of the speed, sometimes a Stale Element Exception will be thrown
        pass