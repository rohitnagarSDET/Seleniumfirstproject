from selenium import webdriver

class Findingelement():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyId = driver.find_element_by_id("name")

        if elementbyId is not None:
            print("We found an elemnet by id")

        elementbyName = driver.find_element_by_name("show-hide")

        if elementbyName is not None:
           print("we have found an element by name")
ff = Findingelement()
ff.test()
