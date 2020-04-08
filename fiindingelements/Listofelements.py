from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElements():

    def test(self):
        baseUrl = "https://letskodeit.teachable.com/pages/practice"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementListByClassname = driver.find_elements_by_class_name("inputs")
        length1 = len(elementListByClassname)

        if elementListByClassname is not None:
            print("ClassName -> Size of the list is: " + str(length1))
        elementListByTagname = driver.find_elements(By.TAG_NAME, "tr")
        length2 = len(elementListByTagname)

        if elementListByTagname is not None:
            print("Tagname -> size of list is:" + str(length2))

ff = ListOfElements()
ff.test()