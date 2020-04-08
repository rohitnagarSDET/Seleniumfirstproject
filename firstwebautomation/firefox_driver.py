from selenium import webdriver

class RunFFTests():
    def testMethod(self):



        driver = webdriver.Firefox()
        driver.get("https://www.flipkart.com/")

ff = RunFFTests()
ff.testMethod()