from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Clickandsendkeys():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        Loginlink = driver.find_element(By.XPATH, "/html//div[@id='navbar']//a[@href='/sign_in']")
        Loginlink.click()

        emailfield = driver.find_element(By.ID, "user_email")
        emailfield.send_keys("test1")

        Passwordfield = driver.find_element(By.ID, "user_password")
        Passwordfield.send_keys("123")

        time.sleep(3)

        emailfield.clear()
        emailfield.send_keys("test")

ff = Clickandsendkeys()
ff.test()

