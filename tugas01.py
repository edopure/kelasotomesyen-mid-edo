
import selenium
import time
from selenium import webdriver

driver = webdriver.Chrome()
url = ['tiket.com','tokopedia.com','orangsiber.com','demoqa.com','automatetheboringstuff.com']

#minimize window
driver.minimize_window()

#looping open url 
for x in url :
    driver.get("https://" + x)
    time.sleep(5)
    print(x + " - " + driver.title)
    
#browser close
driver.close()