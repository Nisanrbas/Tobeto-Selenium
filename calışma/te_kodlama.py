from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

class Test_Kodlama:
    def test_invalid_login(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.kodlama.io/")
        sleep(5)
        login1=driver.find_element(By.XPATH,"/html/body/header/div/div/div/div/ul/li[3]/a")
        login1.click()
        sleep(5)

test1=Test_Kodlama()
test1.test_invalid_login()

