from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://stat.kita.net/stat/kts/pum/ItemImpExpList.screen")
time.sleep(3)
