import csv
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import json
from selenium.webdriver.common.by import By

Email=0
Password=1
Repeat_Password=2


with open('data.csv','r') as csv_file:
    csv_file_reader=csv.reader(csv_file)

    for i in csv_file_reader:

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.w3schools.com/howto/howto_css_register_form.asp")
        driver.implicitly_wait(10)
        driver.find_element(By.XPATH,"//input[@placeholder='Enter email']").send_keys(i[0])
        driver.find_element(By.XPATH, "//input[@placeholder='Enter Password']").send_keys(i[1])
        driver.find_element(By.XPATH, "//input[@placeholder='Repeat Password']").send_keys(i[2])
        driver.find_element(By.XPATH, "//button[@class='w3-button w3-block w3-green w3-padding-16 w3-hover-green w3-opacity-min w3-hover-opacity-off']").click()
        time.sleep(20)