from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

LOGGER.setLevel(logging.WARNING)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5500/index.html")

latitudeInput = driver.find_element(By.ID,"locLat")
longitudeInput = driver.find_element(By.ID,"locLng")
locateButton = driver.find_element(By.ID,"locateButton")

time.sleep(3)

#======================== Test Case 1 ========================
print("====== Test Case 1 ======")

latitudeInput.send_keys("42");
longitudeInput.send_keys("12");
locateButton.click()

if len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Latitude: 42 Longitude: 12')]"))>0:
    print("Locator Verification Test 1: Successful")
else:
    print("Locator Verification Test 1: Failed")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("41.015137") 
longitudeInput.clear()
longitudeInput.send_keys("28.979530")
locateButton.click()

time.sleep(2)

if len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Latitude: 41.015137 Longitude: 28.97953')]"))>0:
    print("Locator Verification Test 2: Successful")
else:
    print("Locator Verification Test 2: Failed")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("86");
locateButton.click()

if(driver.find_element(By.ID,"lngError").is_displayed() or len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Latitude: 86 Longitude: 12')]")) > 0 or not driver.find_element(By.ID,"latError").is_displayed()):
    print("Latitude Error Test: Failed")
else:
    print("Latitude Error Test: Successful")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("41")
longitudeInput.clear()
longitudeInput.send_keys("181")
locateButton.click()

time.sleep(2)

if(driver.find_element(By.ID,"latError").is_displayed() or len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Latitude: 41 Longitude: 181')]")) > 0 or not driver.find_element(By.ID,"lngError").is_displayed()):
    print("Longitude Error Test: Failed")
else:
    print("Longitude Error Test: Successful")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("86")
longitudeInput.clear()
longitudeInput.send_keys("181")
locateButton.click()

time.sleep(2)

if(not driver.find_element(By.ID,"latError").is_displayed() or len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Latitude: 86 Longitude: 181')]")) > 0 or not driver.find_element(By.ID,"lngError").is_displayed()):
    print("Latitude & Longitude Error Test: Failed")
else:
    print("Latitude & Longitude Error Test: Successful")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("Doğancan")
longitudeInput.clear()
longitudeInput.send_keys("Ertuğrul")
locateButton.click()

if(latitudeInput.get_attribute("value") == "Doğancan" or longitudeInput.get_attribute("value") == "Ertuğrul"):
    print("Invalid Character Test: Failed")
else:
    print("Invalid Character Test: Successful")

time.sleep(2)

# time.sleep(5)

driver.close()


