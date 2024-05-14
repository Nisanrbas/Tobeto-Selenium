from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(2)



textarea=driver.find_element(By.NAME,"q")

textarea.send_keys("nisanur baş demirel")
sleep(3)


button=driver.find_element(By.XPATH,"/html/body/div[1]/div[4]")
button.click()
sleep(5)
searchButton=driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]")
sleep(5)
searchButton.click()
firstResault=driver.find_element(By.XPATH,"//*[@id='rso']/div[1]/div/div/div[1]/div/div/span/a")
firstResault.click()


while True:
    continue
  
# sleep(10)

# sleep(3)
# searchButton.click()


# sleep(3)
# searchButton.click()

# searchButton.click()
# sleep(7)
