import os
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyautogui as pag
from dotenv import load_dotenv

def clickMore():
    allbtn=driver.find_elements(By.TAG_NAME,"button")
    for btn in allbtn:
        if btn.text=='More':
            btn.click()
            return

def clickConnect():
    allbtn=driver.find_elements(By.TAG_NAME,"span")
    for btn in allbtn:
        if btn.text=='Connect':
            btn.click()
            return
        
def clickSend():
    allbtn=driver.find_elements(By.TAG_NAME,"button")
    for btn in allbtn:
        if btn.text=='Send':
            btn.click()
            return
        
try:
    serv_obj=Service("E:\Downloads\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_obj)
    driver.get('https://www.linkedin.com')
    driver.maximize_window()
    time.sleep(10)
    USERNAME="joeytrib2148@gmail.com"
    PASSWORD='tanmayee2148'
    username = driver.find_element(By.XPATH,"//input[@name='session_key']")
    password = driver.find_element(By.XPATH,"//input[@name='session_password']")
    username.send_keys(USERNAME)
    password.send_keys(PASSWORD)
    time.sleep(2)
    print('Credentials entered')
    submit = driver.find_element(By.XPATH,"//button[@type='submit']").click()
    
    if driver.title=='Security Verification | LinkedIn':
        print("Complete verification to continue")
    while driver.title=='Security Verification | LinkedIn':
        continue
    
    print('Logged in')
    driver.get('https://www.linkedin.com/in/tanmayee-mali/')
    time.sleep(3)
    #clickMore()
    #clickConnect()
    #clickSend()
    time.sleep(2)
    # connections_element = driver.find_element(By.XPATH, "//span[@class='num-connections']")
    # connections_count = connections_element.text
    
    # print(f"Number of Connections: {connections_count}")
    time.sleep(3)
    # print(moreopt)
    
    # moreopt.click()
    time.sleep(100000)
except Exception as e:
    print('\nEXCEPTION occured\n'+str(e))