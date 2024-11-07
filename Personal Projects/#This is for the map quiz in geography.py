#This is for the map quiz in geography
import time
import mouse
import keyboard
import selenium
from selenium import webdriver 
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.geoguessr.com/quiz/seterra/challenge/JM66C7"
driver.get(url)

country_element = driver.find_element(By.ID, "country-name")
country_name = country_element.text

# Check if the country name matches "Russia"
if country_name == "Russia":
    print("The correct country is Russia!")
else:
    print("The correct country is not Russia.")
driver.get(url)

wordsearch = "Russia"
def findtext(wordsearch):
    # find out if specific text is on the webpage and print result
    if wordsearch in driver.page_source:
        print("True")
        time.sleep(2)
        return
    else:
        print("False")
        time.sleep(2)
        return

findtext(wordsearch)    
def main():
    time.sleep(5)
    mouse.wheel(-3)
    #Use the Russia measurements and add off that for the others :)
    mouse.move(-10000, -10000, absolute=False, duration=0.1)
    mouse.move(1000, 400, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(300, 70, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(0, 100, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(100, 155, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(55, 0, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(0, -40, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(50, -5, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(50, -100, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(0, -40, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(50, 0, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(50, 0, absolute=False, duration=0.1)
    mouse.click('left')
    mouse.move(0, 150, absolute=False, duration=0.1)
    mouse.click('left')