import time
import re
from selenium import webdriver
Timer = 60
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--allow-running-insecure-content")
chrome_options.add_argument(r"--user-data-dir=C:\Users\Tanmya\AppData\Local\Google\Chrome\User Data\Profile 1")
yt="https://www.youtube.com/watch?v=9eHYjbhKuI8"
driver=webdriver.Chrome(r"C:\Users\Tanmya\Downloads\chromedriver_win32\chromedriver.exe",chrome_options=chrome_options)
driver.get(yt)
btn=driver.find_elements_by_tag_name('a')[5]
btn.click()

for i in range(9999):
    time.sleep(Timer)
    driver.refresh()