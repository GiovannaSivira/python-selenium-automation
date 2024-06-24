from selenium import webdriver
from selenium.webdriver import Keys
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

driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//a[@aria-label='Account, sign in']").click()

sleep(6)
driver.find_element(By.ID, 'listaccountNav-signIn').click()
sleep(6)

expected_text = 'Sign into your Target account'
actual_text = driver.find_element(By.XPATH, "//h1[@class= 'styles__StyledHeading-sc-1awz1yh-0 styles__AuthHeading-sc-kz6dq2-2 gfuwhI kcHdEa']").text
print(actual_text)
assert expected_text in actual_text, f'Expected {expected_text} is not in actual text {actual_text}'
print('Test case passed')

driver.find_element(By.ID, 'login')