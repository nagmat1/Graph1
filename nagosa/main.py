# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import time

import pyautogui
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def get_relay_login_credentials():
    return "guljangn1@nevada.unr.edu", "Barlagcy111!"  # TODO


def clickable_element(identifier, sleep_time):
    wait.until(EC.presence_of_element_located(identifier))
    wait.until(EC.element_to_be_clickable(identifier))
    time.sleep(sleep_time)
    driver.find_element(identifier[0], identifier[1]).click()


def relay_login_page():
    email, password = get_relay_login_credentials()
    print(email,password)
    wait.until(EC.presence_of_element_located((By.ID, 'mat-input-0')))
    email_field = driver.find_element(by=By.ID, value='mat-input-0')
    password_field = driver.find_element(by=By.ID, value='mat-input-1')
    email_field.send_keys(email)
    password_field.send_keys(password)
    email_field.send_keys(Keys.RETURN)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    chrome_options = Options()
    print(chrome_options)
    chrome_options.add_argument("--incognito")
    #url = "https://relay.amazon.com/"
    url = "https://www.amazon.com/ap/signin?openid.pape.max_auth_age=86400&openid.return_to=https%3A%2F%2Frelay.amazon.com%2F&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=amzn_relay_desktop_us&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=amzn_relay_desktop_us&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0"
    driver = webdriver.Chrome(options=chrome_options, executable_path='/home/nnazarov/chromedriver')
    driver.get(url)
    wait = WebDriverWait(driver, 15)

    relay_login_page()

    time.sleep(55)


