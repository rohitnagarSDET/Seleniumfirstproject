from selenium import webdriver
import time
class RadioButtonsAndCheckboxes():
    def expedia(self):
        baseUrl = "https://www.expedia.co.in/Flights"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        Flightreturn = driver.find_element_by_id("flight-type-roundtrip-label-flp")
        Flightreturn.click()

        time.sleep(2)
        Flightoneway = driver.find_element_by_id("flight-type-one-way-label-flp")
        Flightoneway.click()

        time.sleep(2)
        FlightMulticity = driver.find_element_by_id("flight-type-multi-dest-label-flp")
        FlightMulticity.click()

        time.sleep(2)
        Flyingfrom = driver.find_element_by_id("flight-origin-flp")
        Flyingfrom.send_keys("New Delhi")

ff = RadioButtonsAndCheckboxes()
ff.expedia()

