from behave import *
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CART = (By.CSS_SELECTOR, ".nav-cart-icon.nav-sprite")
TEXT = (By.CSS_SELECTOR, ".a-row.sc-your-amazon-cart-is-empty")

#@given('Open Amazon homepage')
#def open_amazon_homepage(context):
#    context.driver.get("https://www.amazon.com")


@when('Click on cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART).click()


@then('Verify Amazon Cart is empty')
def verify_cart_empty(context):
    expected_result = context.driver.find_element(*TEXT).text
    sleep(1)
    print(expected_result)
    assert expected_result in "Your Amazon Cart is empty", f' actual text "Your Amazon Cart is empty", but get {expected_result}'

#   Works
