from selenium import webdriver
from selenium.webdriver.common.by import By
import time
class ListofElements():
    def expedia1(self):
        baseUrl = "https://www.expedia.co.in/Flights"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        radioButtonList = driver.find_elements(
            By.XPATH, "//input[contains(@type,'radio') and contains(@name,'flight-type')]")
        size = len(radioButtonList)
        print("'Size of the list:" + str(size))

        for radiobutton in radioButtonList:
            isSelected = radiobutton.is_selected()

            if not isSelected:
               radiobutton.click()
               time.sleep(2)

ff = ListofElements()
ff.expedia1()
