from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import dotenv_values

def scroll(elem):
    driver.execute_script("arguments[0].scrollIntoView();", msg)

def verify(by, value):
    try:
        element = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((by, value))
        )
        return True
    except:
        return False

process = dotenv_values(".env")

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(500)


driver.get("https://discord.com/login")


userElem = driver.find_element(By.ID, 'uid_5')
userElem.clear()
userElem.send_keys(process['USERNAME'])

passElem = driver.find_element(By.ID, 'uid_7')
passElem.clear()
passElem.send_keys(process['PASSWORD'])
passElem.send_keys(Keys.RETURN)

chatElem = driver.find_element(By.CLASS_NAME, 'overflow__87fe8')
print(chatElem)

chatElem.click()


search = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/section/div/div[2]/div[6]/div/div/div[1]/div[2]/div/div/div')
search.click()
search.send_keys(f"before: {(datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')}")
search.send_keys(Keys.RETURN)

time.sleep(2)

old = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/section/header/div[2]/div[2]')
old.click()

oldestMsg = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/section/div/div[1]/ul/li[1]/div[1]/div/div/div[1]/div')
oldestMsg.click()


time.sleep(500)

'''
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/div[3]/li/div
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[88]/div
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[4]/div

'''