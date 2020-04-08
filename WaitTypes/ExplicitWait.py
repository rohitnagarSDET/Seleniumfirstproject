from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

class ExplicitWaitDemo1():
    def test(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get(baseUrl)
        driver.find_element(By.ID, "tab-flight-tab-hp").click()
        driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
        driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
        driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("04/24/2020")
        returnDate = driver.find_element(By.ID, "flight-returning-hp-flight")
        returnDate.clear()
        returnDate.send_keys("05/25/2020")
        driver.find_element(By.CSS_SELECTOR, "[data-gcw-key='hp-flight'] .btn-primary").click()
        wait = WebDriverWait(driver, 10, poll_frequency=1, ignored_exceptions=[NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException])
        element = wait.until(EC.element_to_be_clickable((By.ID, "stopFilter_stops-0")))
        element.click()

        time.sleep(2)
ff = ExplicitWaitDemo1()
ff.test()
