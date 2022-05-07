
import time

from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv(find_dotenv())

web_url = os.environ.get('WEB_URL')
email = os.environ.get("EMAIL")
print(email)
print(web_url)


def login_site():
    driver = webdriver.Chrome('chromedriver')
    driver.get(web_url)
    print(driver.title)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[3]/div/div[2]/div/button'))).click()

    textbox = '/html/body/div/div/div[3]/div/div[2]/div/div[2]/div/div/div/div/input'
    f = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, textbox)))

    f.send_keys(email)
    butclick = '/html/body/div/div/div[3]/div/div[2]/div/div[2]/div/button'

    f = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, butclick)))
    f.click()

    print("Done")
    time.sleep(10)
    driver.close()


def _main():
    login_site()


if __name__ == "__main__":
    # pass
    _main()
