from selenium import webdriver
class Chromedriverdemo():
    def testmethodchrome(self):
        driver = webdriver.Chrome()
        driver.get("https://www.amazon.in/")

tt = Chromedriverdemo()
tt.testmethodchrome()