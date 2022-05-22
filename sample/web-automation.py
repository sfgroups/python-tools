import os
import time

from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

load_dotenv(find_dotenv())

web_url = os.environ.get('WEB_URL')
email = os.environ.get("EMAIL")
print(email)
print(web_url)


# https://github.com/WPIRoboticsEngineering/Workday-Automation/blob/master/invoice.py

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


def login2():
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    driver = webdriver.Chrome(options=options)
    driver.get('https://login.live.com/login.srf')
    driver.implicitly_wait(10)
    print("Page Title is : %s" % driver.title)

    EMAILFIELD = (By.ID, "i0116")
    PASSWORDFIELD = (By.ID, "i0118")
    NEXTBUTTON = (By.ID, "idSIButton9")

    email = 'test@gmail.com'
    passowrd = 'password'

    # wait for email field and enter email
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(email)

    # Click Next
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

    # wait for password field and enter password
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(passowrd)

    # Click Login - same id?
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()

    verify_id = "iLandingViewAction"
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.ID, verify_id)))
    element.click()
    wait = WebDriverWait(driver, 10)
    val = input("Enter your value: ")
    print(val)

    id_proof2 = "iProof2"
    element = wait.until(EC.element_to_be_clickable((By.ID, id_proof2)))
    element.click()

    id_verify_online = "iSelectProofAction"
    element = wait.until(EC.element_to_be_clickable((By.ID, id_verify_online)))
    element.click()

    time.sleep(130)
    driver.close()


def login():
    email_ID = "YourEmail@Gmail.com"
    Password = "Password"

    driver = webdriver.Chrome()
    driver.set_page_load_timeout(10)
    driver.get("https://outlook.office365.com/mail/inbox")

    try:
        element = WebDriverWait(driver, 10).until
        (
            # EC.presence_of_element_located((By.ID, "myDynamicElement"))
            EC.url_contains("login.microsoftonline.com/common/oauth2/authorize")
        )
    finally:
        print("2nd Login Page Reached.")
        print(driver.current_url)

        # Login
        driver.find_element_by_id("i0116").send_keys(email_ID)
        # driver.find_element_by_id("i0118").send_keys(Password) #passwordBrowserPrefill
        print("Login Entered")
        driver.find_element_by_xpath('//*[@id="idSIButton9"]').submit()


def login4():
    driver = webdriver.Chrome('chromedriver')
    # open github.com login
    driver.get("http://www.github.com/login")

    # My githun credentials
    my_username = "MyUserName"
    my_password = "MyPassword123@"

    # access github login username input
    username_input_box = driver.find_element_by_name("login")

    # access github login password input
    password_input_box = driver.find_element_by_name("password")

    # access github signup button
    sign_up_button = driver.find_element_by_name("commit")

    # clear the placeholders data
    username_input_box.clear()
    password_input_box.clear()

    # fill login credentials
    username_input_box.send_keys(my_username)
    time.sleep(2)  # 2 second time gap between filling username and password
    password_input_box.send_keys(my_password)

    time.sleep(2)  # 2 second time delay

    # hit the login button
    sign_up_button.click()
    # automatically close the driver after 30 seconds
    time.sleep(30)
    driver.close()


def post_with_js():
    driver = webdriver.Chrome('chromedriver')
    jsrequest = '''var xhr = new XMLHttpRequest();
    xhr.open('POST', '{{URL}}', false);
    xhr.send(param1=value&param2=value2');
    return xhr.response;'''

    result = driver.execute_script(jsrequest);

    # access_token = read_access_token()
    # new_data = {
    #     "nsp_svc": "AppPromote.Developer.getRole",
    #     "access_token": access_token,
    #     "nsp_fmt": "JSON",
    #     "nsp_ts": setting.nsp_ts,
    # }
    # new_driver = seleniumrequests.Chrome()
    # time.sleep(2)
    # response = new_driver.request('POST', 'https://api.xxxx.com/rest.php', data=new_data)
    # print
    # response.text


def _main():
    # login_site()
    login2()


if __name__ == "__main__":
    # pass
    _main()
