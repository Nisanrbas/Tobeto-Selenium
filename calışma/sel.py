from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.com/")
sleep(5)
input = driver.find_element(By.NAME,"q")
input.send_keys("kodlamaio")
searchButton = driver.find_element(By.NAME, "btnK")
sleep(2)
searchButton.click()
sleep(2)
firstResault=driver.find_element(By.XPATH,"/html/body/div[4]/div/div[12]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a")
firstResault.click()
listOfCourses=driver.find_elements(By.CLASS_NAME,"course-listing")
print(f"kodlama.io da  {len(listOfCourses)} adet kurs var ")
# sleep(10)
while True:
    continue