from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import dotenv_values
import csv

def scroll(elem):
    driver.execute_script("arguments[0].scrollIntoView();", elem)

def verify(by, value):
    try:
        elem = driver.find_element(by, value)
    except NoSuchElementException:
        return False
    return elem

process = dotenv_values(".env")

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(1)


driver.get("https://discord.com/login")


userElem = driver.find_element(By.ID, 'uid_5')
userElem.clear()
userElem.send_keys(process['USERNAME'])

passElem = driver.find_element(By.ID, 'uid_7')
passElem.clear()
passElem.send_keys(process['PASSWORD'])
passElem.send_keys(Keys.RETURN)

WebDriverWait(driver, 8).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'overflow__87fe8'))
)

chatElem = driver.find_element(By.CLASS_NAME, 'overflow__87fe8')

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

i = 0
date = ""
user = ""

data = []

while True:
    try:
        i += 1

        if (i % 10 == 0):
            file = open('data.csv', 'a', newline='')
            csv.writer(file).writerows(data)
            file.close()
            data = []

        if (verify(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]')):
            if (i % 25 == 0):
                element = driver.find_element(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]')
                scroll(element)

            dateElem = verify(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]/div/div[1]/div/div/div[2]/span')
            if(dateElem):
                datetime = dateElem
                date = datetime.text

                user = "SYSTEM"

                # textElem = verify(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]/div/div[1]/div/div/div[2]')
                text = "You Missed a call from SteakFisher"

                data.append([date, user, text])

                continue
            
            dateElem = verify(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]/div/div[1]/h3/span[2]')
            if (dateElem):
                datetime = dateElem
                date = datetime.text

                userElem = verify(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]/div/div[1]/h3/span[1]/span')
                user = userElem.text

                textElem = verify(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]/div/div[1]/div/span')
                if (textElem):
                    text = textElem.text
                else:
                    text = "Image/Vid/Gif"

                data.append([date, user, text])

                continue

            dateElem = verify(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]/div/div[1]/div/span')
            if (dateElem):

                textElem = verify(By.XPATH, f'/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[{i}]/div/div[1]/div/span')
                text = textElem.text

                if (textElem):
                    text = textElem.text
                else:
                    text = "Image/Vid/Gif"

                data.append([date, user, text])

                continue

            else:
                continue
    except:
        break

file = open('data.csv', 'a', newline='')
csv.writer(file).writerows(data)
file.close()
data = []

time.sleep(1500)

'''
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/div[3]/li/div
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[88]/div
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[4]/div

/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[1]/div
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div[1]/div/ol/li[2]/div

/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div/div/ol/li[6]/div/div[1]/div/span
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div/div/ol/li[7]/div/div[1]/div/span
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div/div/ol/li[12]/div/div[1]/div/span
/html/body/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/main/div[1]/div/div/ol/li[13]/div/div[1]/div/span
'''