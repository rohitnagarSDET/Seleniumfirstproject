from selenium import webdriver

class Browserinteractions():
    def test(self):
        baseUrl = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Firefox()
        driver.maximize_window()

        driver.get(baseUrl)
        title = driver.title
        print("Title of web page is:" + title)
        currentUrl = driver.current_url
        print("Current url of web page is:" + currentUrl)
        driver.refresh()
        print("browser refreshed first time")
        driver.get(driver.current_url)
        driver.get("https://sso.teachable.com/secure/42299/users/sign_up?reset_purchase_session=1")
        driver.back()
        print("go one step back")
        driver.forward()
        print("one step forward")

        pagesource = driver.page_source
        driver.quit()
ff = Browserinteractions()
ff.test()






