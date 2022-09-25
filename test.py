
from turtle import delay
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://inline.app/booking/-MaXEDw_rk9TrqlPI1GT:inline-live-2/-MaXiZkmvvNWFe-osWj5/form')
driver.maximize_window()

driver.execute_script("window.scrollBy(305, 1200)","") 
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"adult-picker\"]"))))




# select how many people 
# driver.find_element("xpath", '//*[@id=\"adult-picker\"]').click()

# option[2] -> 1 adult, option[3] -> 2 adults, ..., upto 8 adults
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id=\"adult-picker\"]'))).click()
driver.find_element("xpath", '//*[@id=\"adult-picker\"]/option[5]').click()

##********** test another website********
driver.execute_script("window.scrollBy(305, 1200)","") 
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"book-now-content\"]/div[2]/button[3]"))))
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"book-now-action-bar\"]/div[2]/button"))))
# driver.find_element("xpath", "//*[@id=\"book-now-action-bar\"]/div[2]/button").click()
##***************************************
# the code i want for 國秀食堂
# click "book now" bottom
# driver.find_element_by_xpath(“//*[@id="book-now-action-bar"]/div/button”).click()

# enter name
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"name\"]"))))
name = driver.find_element("xpath", "//*[@id=\"name\"]")
name.clear()
name.send_keys("趙佑軒")

# click gender bottom
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"gender-male\"]"))))

# enter phone number
number = driver.find_element("xpath", "//*[@id=\"phone\"]")
number.clear()
number.send_keys("0908816118")

# enter email
email = driver.find_element("xpath", "//*[@id=\"email\"]")
email.clear()
email.send_keys("xuann.cn@gmail.com")

# select "用餐目的"
driver.find_element("xpath", "//*[@id=\"contact-form\"]/section/div[5]/div[1]/div[4]").click()

# click "我已閱讀並同意"
driver.execute_script("window.scrollBy(305, document.body.scrollHeight)","") 
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"contact-form\"]/div/div[2]/label"))))

# click "確認訂位"
driver.execute_script("arguments[0].click();", WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"contact-form\"]/div/button[1]"))))

result = ''
while(result != 'check'):
    result = input("Enter \"check\" to stop the program: ")



