from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Screenshots():

    def test(self):
        baseUrl = "https://www.airtel.in/s/selfcare?normalLogin"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(3)

        driver.find_element(By.NAME, "mobileNumber").send_keys("9560622708")

        driver.find_element(By.NAME, "password").send_keys("abc")
        driver.find_element(By.CSS_SELECTOR, "#loginButtonSpan").click()
        destinationFileName = "C:\\Users\\rohit\\Desktop\\Screenshot\\test.png" # Mac
        # destinationFileName = "C:\\atomar\\Desktop" -> Windows

        try:
            driver.save_screenshot(destinationFileName)
            print("Screenshot saved to directory --> :: " + destinationFileName)
        except NotADirectoryError:
            print("Not a directory issue")

ff = Screenshots()
ff.test()