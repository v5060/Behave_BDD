from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@given('Open Browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://demo.guru99.com/test/newtours/")
    # raise NotImplementedError(u'STEP: Given Open Browser')


@when('providing valid username "{username}" and password "{password}"')
def valid_username_password(context, username, password):
    context.driver.find_element(By.NAME, "userName").send_keys(username)
    context.driver.find_element(By.NAME, "password").send_keys(password)
    context.driver.find_element(By.NAME, "submit").click()
    # raise NotImplementedError(u'STEP: When providing valid username and password')


@then('Verifying home page')
def verify_home_page(context):
    assert "Login: Mercury Tours" == context.driver.title
    time.sleep(3)
    # raise NotImplementedError(u'STEP: Then Verifying home page')


@then('verify Success Message')
def verify_success_(context):
    try:
        text = context.driver.find_element(By.XPATH, "//h3[text()='Login Successfully']")
    except:
        context.driver.close()
        assert False, "Test Case has Failed"

    if text == "Login Successfully":
        context.driver.close
        assert True, "Test Case Passed"


@when('verify login by using below query')
def verify_table_data(context):
    for r in context.table:
        context.driver.find_element(By.NAME, "userName").send_keys(r["username"])
        context.driver.find_element(By.NAME, "password").send_keys(r["password"])
        context.driver.find_element(By.NAME, "submit").click()

#
# @when('providing wrong username and password')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When providing wrong username and password')
#
#
# @then('Verification should remain on same page')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then Verification should remain on same page')
#
