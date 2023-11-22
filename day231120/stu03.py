from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://www.naver.com")



login = driver.find_element(By.CLASS_NAME, "MyView-module__my_login___tOTgr")
login.click()


id = driver.find_elements(By.CLASS_NAME, "input_text")[0]
id.click()
id.send_keys("abcd")

pw = driver.find_elements(By.CLASS_NAME, "input_text")[1]
pw.click()
pw.send_keys("1234")

login_btn = driver.find_element(By.CLASS_NAME, "btn_login_wrap")
login_btn.click()
