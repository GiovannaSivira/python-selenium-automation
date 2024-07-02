rom selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')


#CCS LOCATORS
from selenium.webdriver.common import by

#Amazon Logo
driver.find_element(by.CSS_SELECTOR, "[role='img']")

#Create Account text
driver.find_element(by.CSS_SELECTOR, ".a-spacing-small")

#Your name field
driver.find_element(by.CSS_SELECTOR, "#ap_customer_name")

#Email field
driver.find_element(By.CSS_SELECTOR, "#ap_email")

#Password field
driver.find_element(By.CSS_SELECTOR, "#ap_password")

#Re-enter password field
driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

#"Create your Amazon account" or "Continue" yellow button
driver.find_element(By.CSS_SELECTOR, "#continue")

#Conditions of Use link
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*= 'ap_register_notification_condition_of_use']")

#Privacy Notice link
driver.find_element(By.CSS_SELECTOR, "div#legalTextRow a[href*= 'ap_register_notification_condition_of_use']")

#Sing in link
driver.find_element(By.CSS_SELECTOR, "a.a-link-emphasis")