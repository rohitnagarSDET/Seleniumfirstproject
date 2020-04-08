from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class CalendarSelection():






    def test2(self):
        baseUrl = "http://www.expedia.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        # Click flights tab
        driver.find_element_by_id("tab-flight-tab-hp").click()
        # Click departing field
        driver.find_element_by_id("flight-departing-hp-flight").click()
        # Expedia website has changed the DOM after the lecture was made
        # Updated new xpath
        calMonth = driver.find_element(By.CSS_SELECTOR,
                                       ".datepicker-cal .datepicker-cal-month:nth-child(4) .datepicker-cal-month-header")
        allValidDates = calMonth.find_elements(By.TAG_NAME, "button")

        time.sleep(2)

        for date in allValidDates:
            if date.text == "31":
                date.click()


ff = CalendarSelection()
ff.test2()