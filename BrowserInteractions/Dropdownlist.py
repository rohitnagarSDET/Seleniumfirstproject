from selenium import webdriver
import time
from selenium.webdriver.support.select import Select

class DropdownSelect():
    def test(self):
        baseUrl = "https://learn.letskodeit.com/p/practice"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(10)

        element = driver.find_element_by_id("carselect")
        sel = Select(element)
        time.sleep(2)

        sel.select_by_value("benz")
        print("Select Benz by value")
        time.sleep(2)
        sel.select_by_index("2")
        print("Select Honda by index")
        time.sleep(2)
        sel.select_by_visible_text("BMW")
        print("Select BMW by Visible text")
        time.sleep(2)
        sel.select_by_index(1)
        print("select Honda by index")

ff = DropdownSelect()
ff.test()





