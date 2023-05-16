from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('http://www.google.com')

search_box = browser.find_element(By.NAME, 'q')
search_box.send_keys("automatización")
search_box.send_keys(Keys.ENTER)

page = browser.find_element(By.CSS_SELECTOR, ".Z26q7c .xvfwl").click()
title = browser.find_element(By.ID, "La_Revolución_Industrial_en_Europa_Occidental").click()
browser.save_screenshot('wikipedia.png')

browser.close()
