from selenium import webdriver
from selenium.webdriver.common.by import By
import time

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

if len(driver.find_elements_by_xpath("//*[contains(text(), 'Latitude: 42 Longitude: 12')]"))>0:
    print("Locator Verification Test: Successful")
else:
    print("Locator Verification Test: Failed")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("86");
locateButton.click()

if(driver.find_element_by_id("lngError").is_displayed() or len(driver.find_elements_by_xpath("//*[contains(text(), 'Latitude: 86 Longitude: 12')]")) > 0 or not driver.find_element_by_id("latError").is_displayed()):
    print("Latitude Test: Failed")
else:
    print("Latitude Test: Successful")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("41")
longitudeInput.clear()
longitudeInput.send_keys("181")
locateButton.click()

time.sleep(2)

if(driver.find_element_by_id("latError").is_displayed() or len(driver.find_elements_by_xpath("//*[contains(text(), 'Latitude: 41 Longitude: 181')]")) > 0 or not driver.find_element_by_id("lngError").is_displayed()):
    print("Longitude Test: Failed")
else:
    print("Longitude Test: Successful")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("86")
longitudeInput.clear()
longitudeInput.send_keys("181")
locateButton.click()

time.sleep(2)

if(not driver.find_element_by_id("latError").is_displayed() or len(driver.find_elements_by_xpath("//*[contains(text(), 'Latitude: 86 Longitude: 181')]")) > 0 or not driver.find_element_by_id("lngError").is_displayed()):
    print("Latitude & Longitude Test: Failed")
else:
    print("Latitude & Longitude Test: Successful")

# time.sleep(5)

# driver.close()


