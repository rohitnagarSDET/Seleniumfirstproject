from selenium import webdriver

class FindbyXpathCss():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyXpath = driver.find_element_by_xpath("//input[@id='name']")

        if elementbyXpath is not None:
            print("We found an elemnet by Xpath")

        elementbyCss = driver.find_elements_by_css_selector("input#displayed-text")

        if elementbyCss is not None:
           print("we have found an element by css")
ff = FindbyXpathCss()
ff.test()
