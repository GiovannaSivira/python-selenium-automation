from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@given('Open target circle page')
def open_target_circle(context):
    context.driver.get('https://www.target.com/l/target-circle/-/N-pzno9/')
    # sleep(6)
    context.driver.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[class='cell-item-content']")))

@then('Verify circle has {number} cells')
def verify_circle_benefit_cells(context, number):
    number = int(number)
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[class='cell-item-content']")
    assert len(cells) == number, f'Expected {number} cells but got {len(cells)}'
    assert len(cells)> 0
