from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys
import logging
from selenium.webdriver.remote.remote_connection import LOGGER
from random import randint

LOGGER.setLevel(logging.WARNING)

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5500/index.html")

latitudeInput = driver.find_element(By.ID,"locLat")
longitudeInput = driver.find_element(By.ID,"locLng")
currentLat = driver.find_element(By.ID,"currentLat")
currentLng = driver.find_element(By.ID,"currentLng")
locateButton = driver.find_element(By.ID,"locateButton")

time.sleep(3)

#Test two valid inputs and four invalid inputs
#For invalid inputs corresponding error messages should shown on page
#if both of the inputs are invalid, both of the error messages should show
#Inputs should not accept any charachter other than dot and number
#If invalid charachter is provided, simply rejects and stays empty
#======================== Test Case 1 ========================
print("====== Test Case 1 ======")

latitudeInput.send_keys("42");
longitudeInput.send_keys("12");
locateButton.click()

if len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Latitude: 42 Longitude: 12')]"))>0:
    print("Locator Verification Test 1: Successful")
else:
    print("Locator Verification Test 1: Failed")
    sys.exit()

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
    sys.exit()

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("86");
locateButton.click()

if(driver.find_element(By.ID,"lngError").is_displayed() or len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Latitude: 86 Longitude: 12')]")) > 0 or not driver.find_element(By.ID,"latError").is_displayed()):
    print("Latitude Error Test: Failed")
    sys.exit()
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
    sys.exit()
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
    sys.exit()
else:
    print("Latitude & Longitude Error Test: Successful")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("Do??ancan")
longitudeInput.clear()
longitudeInput.send_keys("Ertu??rul")
locateButton.click()

if(latitudeInput.get_attribute("value") == "Do??ancan" or longitudeInput.get_attribute("value") == "Ertu??rul"):
    print("Invalid Character Test: Failed")
    sys.exit()
else:
    print("Invalid Character Test: Successful")

time.sleep(2)

#There are already two points defined on the map which are labeled "North Pole" & "Your Location"
#If exactly same location given as these infowindows, new infowindow for the input should close the corresponding existing infowindow
#If  input is moved to a different place, close infowindow should reopen with same label
#Tests by first moves to "Your Location", than to a different location than to "North Pole" and again than to a different location
#Checks if existing infowindows are closed properly
#======================== Test Case 2 ========================
print("====== Test Case 2 ======")

currentLatVal = float(currentLat.get_attribute("innerHTML")[len("Current Latitude : "):])
currentLngVal = float(currentLng.get_attribute("innerHTML")[len("Current Longitude : "):])

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("41.015137") 
longitudeInput.clear()
longitudeInput.send_keys("28.979530")
locateButton.click()

if(len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Your Location')]")) <= 0 or len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'North Pole')]")) <= 0):
    print("Current Location Label Conflict and North Pole Label Conflict Test 1: Failed")
    sys.exit()
else:
    print("Current Location Label Conflict and North Pole Label Conflict Test 1: Successful")

time.sleep(2)

longitudeInput.clear()
latitudeInput.clear()
latitudeInput.send_keys(currentLatVal)
longitudeInput.send_keys(currentLngVal)
locateButton.click()

if(len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Your Location')]")) > 0 or len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'North Pole')]")) <= 0):
    print("Current Location Label Conflict and North Pole Label Conflict Test 2: Failed")
    sys.exit()
else:
    print("Current Location Label Conflict and North Pole Label Conflict Test 2: Successful")

time.sleep(2)

latitudeInput.clear()
latitudeInput.send_keys("41.015137") 
longitudeInput.clear()
longitudeInput.send_keys("28.979530")
locateButton.click()

if(len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Your Location')]")) <= 0 or len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'North Pole')]")) <= 0):
    print("Current Location Label Conflict and North Pole Label Conflict Test 3: Failed")
    sys.exit()
else:
    print("Current Location Label Conflict and North Pole Label Conflict Test 3: Successful")

time.sleep(2)

longitudeInput.clear()
latitudeInput.clear()
latitudeInput.send_keys("72.68")
longitudeInput.send_keys("80.65")
locateButton.click()

if(len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'North Pole')]")) > 0 or len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), 'Your Location')]")) <= 0):
    print("Current Location Label Conflict and North Pole Label Conflict Test 4: Failed")
    sys.exit()
else:
    print("Current Location Label Conflict and North Pole Label Conflict Test 4: Successful")

#Checks if distance between current location of the device and the north pole exists
#if it does, than compares to possible min and max values of such distance
#min and max values are gathered using Google Maps by taking distance between closest and farthest points of Ankara and North Pole
#Tests if shown value is in between min and max value range
#======================== Test Case 3 ========================
print("====== Test Case 3 ======")

time.sleep(2)
if(len(driver.find_elements(By.ID,"distancePoints")) <= 0):
    print("Distance Between Two Points Label Test: Failed")
    sys.exit()
else:
    print("Distance Between Two Points Label Test: Successful")

    distancePoints = driver.find_element(By.ID,"distancePoints")
    distancePointStr = distancePoints.get_attribute("innerHTML")
    distancePointValue = float(distancePointStr[len("Distance between markers: "):-4])

    if(distancePointValue >= 4370.05 or distancePointValue <= 4572.28):
        print("Distance Between Two Points Value Test: Successful")
    else:
        print("Distance Between Two Points Value Test: Failed")
        sys.exit()

#Checks if distance between current location of the device and the Moon exists
#if it does, than compares to possible min and max values of such distance
#Possible min and max values are gathered using Google
#Tests if shown value is in between min and max value range
#======================== Test Case 4 ========================
print("====== Test Case 4 ======")

time.sleep(2)
if(len(driver.find_elements(By.ID,"distanceMoon")) <= 0):
    print("Distance Between Point and Moon Label Test: Failed")
    sys.exit()
else:
    print("Distance Between Point and Moon Label Test: Successful")

    distanceMoon = driver.find_element(By.ID,"distanceMoon")
    distanceMoonStr = distanceMoon.get_attribute("innerHTML")
    distanceMoonValue = float(distanceMoonStr[len("Distance between Moon and Point: "):-4])

    if(distanceMoonValue >= 363105.021 or distanceMoonValue <= 405696.31):
        print("Distance to Moon Value Test: Successful")
    else:
        print("Distance to Moon Value Test: Failed")
        sys.exit()

#Rapidly enters 10 different random valid locations to the map every 0.5 seconds
#Tests if previously opened infowindows closed properly when a new input is submitted
#At the end of the test only the infowindow of the last input should remain
#======================== Test Case 5 ========================
print("====== Test Case 5 ======")
prevLats = []
prevLngs = []

for i in range(0,10):
    lat = randint(-85,85)
    lng = randint(-180,180)

    time.sleep(0.5)

    latitudeInput.clear()
    latitudeInput.send_keys(str(lat))
    longitudeInput.clear()
    longitudeInput.send_keys(str(lng))
    locateButton.click()

    prevLats.append(lat)
    prevLngs.append(lng)

for i in range(0,9):
    value = "Latitude: " + str(prevLats[i]) + " Longitude: " + str(prevLngs[i])

    if(len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), '%s')]"%value)) > 0):
        print("Rapid Valid Input Test: Failed")
        print("At Lat: %s Lng: %s"%(str(prevLats[i]),str(prevLngs[i])))
        sys.exit()

value = "Latitude: " + str(prevLats[9]) + " Longitude: " + str(prevLngs[9])    
if(len(driver.find_elements(by=By.XPATH, value="//*[contains(text(), '%s')]"%value)) <= 0):
    print("Rapid Valid Input Test: Failed")
    print("At Lat: %s Lng: %s"%(str(prevLats[9]),str(prevLngs[9])))
    sys.exit()
else:
    print("Rapid Valid Input Test: Successful")

print("All Tests Passed Successfully!")
time.sleep(2)
driver.close()


