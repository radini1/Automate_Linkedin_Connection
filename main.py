from selenium import webdriver 
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.linkedin.com')
time.sleep(2)

## Log in to our account 
username = driver.find_element(By.XPATH, "//*[@id='session_key']")
password = driver.find_element(By.XPATH, "//*[@id='session_password']")

username.send_keys('raadin.dev@gmail.com')
password.send_keys('<YOUR PASSWORD>')
time.sleep(2)

submit = driver.find_element(By.XPATH, "//*[@id='main-content']/section[1]/div/div/form/div[2]/button").click()

## Add contacts 
# put any people url you want.
driver.get("https://www.linkedin.com/search/results/all/?keywords=english%20teacher&origin=QUERY_SUGGESTION&sid=9-s")
time.sleep(2)

all_buttons = driver.find_elements(By.TAG_NAME, "button")
connect_buttons = [i for i in all_buttons if i.text== "Connect"]

# we want to click and click in all the connect buttons 
for btn in connect_buttons:
    driver.execute_script("arguments[0].click();", btn)
    time.sleep(2)

    # (finally we have to click on send button).
    send_connection = driver.find_element(By.XPATH, "//button[@aria-label='Send now']")
    driver.execute_script("arguments[0].click();", send_connection)
    
    # this for those who we can't send connection
    close = driver.find_element(By.XPATH, "//button[@arial-label='Dismiss']")
    driver.execute_script("arguments[0].click();", close)
    time.sleep(2)
