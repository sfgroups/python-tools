import csv
import json
import time
from pathlib import Path

import cv2
from bs4 import BeautifulSoup
from dotenv import find_dotenv, dotenv_values
from loguru import logger
from pytesseract import image_to_string
from requests.structures import CaseInsensitiveDict
from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


def get_captcha(file_name):
    img = cv2.imread(str(file_name))
    gry = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (h, w) = gry.shape[:2]
    gry = cv2.resize(gry, (w * 2, h * 2))
    cls = cv2.morphologyEx(gry, cv2.MORPH_CLOSE, None)
    thr = cv2.threshold(cls, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    captcha = image_to_string(thr)
    return captcha


def base_dir():
    download_folder = Path(Path.home(), 'Downloads', 'Test')
    if not download_folder.exists():
        download_folder.mkdir()
    return download_folder


def get_patta_as_list():
    filename = Path(base_dir(), "pattas.txt")
    with open(filename, "r") as f:
        content_list = f.readlines()

    c = [x.strip() for x in content_list]
    return c


def get_survey_list():
    download_folder = base_dir()
    in_filename = Path(download_folder, "area.csv")
    lines = []
    with open(in_filename, "r", encoding='UTF8', newline='') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[0].strip().casefold() != 'Patta'.casefold():
                lines.append(','.join(row))

    return lines


def setup_browser_driver():
    download_folder = base_dir()
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }

    prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings),
             'savefile.default_directory': str(download_folder)}

    options.add_experimental_option('prefs', prefs)
    options.add_argument('--kiosk-printing')

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    return driver


def get_patta_fmb(ispatta=True):
    download_folder = base_dir()
    config = CaseInsensitiveDict(dotenv_values(find_dotenv()))

    dc = config['DISTRICT_CODE']
    tc = config['TALUK_CODE']
    vc = config['VILLAGE_CODE']

    driver = setup_browser_driver()

    try:
        if ispatta:
            web_url = config['TN_URL']
            for patta in get_patta_as_list():
                download_filename = str(patta) + ".pdf"
                if Path(download_folder, download_filename).exists():
                    logger.info('Patta Already downloaded : {}'.format(patta))
                else:
                    find_patta_fmb(driver, web_url, dc, tc, vc, patta, None, None, download_folder, download_filename)
                    time.sleep(1)
        else:
            web_url = config['ESERVICE_HOME']
            for sur in get_survey_list():
                row = sur.split(',')
                surveyno = row[1]
                subdivno = row[2]
                download_filename = f"fmb_{surveyno}_{subdivno.lower()}.html"
                if Path(download_folder, download_filename).exists():
                    logger.info(f'FMB Already downloaded : {download_filename}')
                else:
                    logger.info(f'Trying to downloaded : {download_filename}')
                    find_patta_fmb(driver, web_url, dc, tc, vc, None, surveyno, subdivno, download_folder,
                                   download_filename)
                    time.sleep(5)

    finally:
        if driver:
            driver.close()
            driver.quit()


def find_patta_fmb(driver, web_url, dc, tc, vc, patta, surveyno, subdivno, download_folder, download_filename):
    driver.get(web_url)
    if subdivno:
        driver.find_element(By.XPATH, "//a[contains(@href, 'chittaNewRuralFMBTamil')]").click()
        time.sleep(5)

    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "districtCode"))))
    select.select_by_value(dc)
    time.sleep(2)
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "talukCode"))))
    select.select_by_value(tc)
    time.sleep(2)
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "villageCode"))))
    select.select_by_value(vc)
    time.sleep(2)

    if patta:
        save_patta(driver, patta, download_folder, download_filename)
    else:
        save_fmb(driver, surveyno, subdivno, download_folder, download_filename)


def save_fmb(driver, surveyno, subdivno, download_folder, download_filename):
    time.sleep(1)
    driver.find_element(By.NAME, "surveyNo").send_keys(surveyno)
    actions = ActionChains(driver)
    actions.send_keys(Keys.TAB)
    actions.perform()
    time.sleep(2)
    select = Select(WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "subdivNo"))))
    # for options in select.options:
    #     print(options.text)
    select.select_by_value(subdivno)
    time.sleep(1)

    filename = Path(download_folder, 'test.png')
    with open(filename, "wb") as f:
        element = driver.find_element(By.ID, "captcha_name")
        f.write(element.screenshot_as_png)

    captcha = get_captcha(filename)

    logger.info(f"Captcha {captcha}")
    driver.find_element(By.NAME, "captcha").send_keys(captcha)
    time.sleep(2)

    driver.find_element(By.ID, 'myanc').click()
    time.sleep(10)

    # get current window handle
    p = driver.current_window_handle
    # get first child window
    chwd = driver.window_handles
    for w in chwd:
        # switch focus to child window
        if w != p:
            driver.switch_to.window(w)
            break

    time.sleep(5)

    html_filename = Path(download_folder, download_filename)
    logger.info(f"Saving file : {html_filename}")
    with open(html_filename, "w") as f:
        f.write(driver.page_source)

    if p != driver.current_window_handle:
        driver.close()
        driver.switch_to.window(p)
    else:
        logger.warning("New window didn't open")


def save_patta(driver, patta, download_folder, download_filename):
    xpath = "/html/body/div[1]/section/table/tbody/tr[2]/td/table/tbody/tr/td/div/form/div[14]/div[2]/input[1]"
    radio_button = driver.find_element(By.XPATH, xpath)
    radio_button.click()

    time.sleep(2)
    driver.find_element(By.NAME, "pattaNo").send_keys(patta)

    filename = Path(download_folder, 'test.png')
    with open(filename, "wb") as f:
        element = driver.find_element(By.ID, "captcha_name")
        f.write(element.screenshot_as_png)

    captcha = get_captcha(filename)

    print(captcha)
    driver.find_element(By.NAME, "captcha").send_keys(captcha)

    time.sleep(5)
    html_filename = Path(download_folder, download_filename.replace('.pdf', '.html'))

    with open(html_filename, "w") as f:
        f.write(driver.page_source)

    driver.execute_script("document.title = \'{}\'".format(download_filename))
    driver.execute_script('window.print();')

    time.sleep(2)


def create_area_file():
    download_folder = base_dir()
    out_filename = Path(download_folder, "area.csv")
    with open(out_filename, "w", encoding='UTF8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Patta", "Survey No", "Sub Division", "Area", "Cents", "Acer"])
        for patta in get_patta_as_list():
            filename = Path(download_folder, str(patta) + '.html')
            lines = parse(patta, filename)
            for line in lines:
                if len(line) > 4:
                    writer.writerow(line)

    logger.info(f"Area file:  {out_filename}")


def parse(patta, filename):
    ret_value = []
    with open(filename) as fp:
        soup = BeautifulSoup(fp, 'html.parser')

        for table in soup.find_all('table'):
            count = 1
            for subtable in table.find_all('table'):
                # print("==== table ===== {}".format(count))
                # Second table has the data
                if count == 2:
                    for row in subtable.find_all("tr"):
                        c = 1
                        isprint = False
                        survey_no = ""
                        sub_number = ""
                        area = ""
                        for col in row.find_all("td"):
                            if c == 1:
                                data = col.text.strip()
                                if data.isnumeric():
                                    isprint = True
                                    survey_no = data
                            if isprint:
                                if c == 2:
                                    sub_number = col.text.strip()
                                elif c == 3:
                                    area = col.text.strip()

                            c += 1

                        if isprint:
                            cents = convert_hectare_to_acer(area)
                            acer = convert_cents_acer(cents)
                            ret_value.append( [patta, survey_no, sub_number, area, f"{cents:.4}", f"{acer:.2}"])

                count += 1

        return ret_value


def convert_hectare_to_acer(hectare):
    (w, f) = hectare.split('-')
    cents = 0
    if int(w) > 0:
        cents = int(w) * 100

    cents += float(f) * 2.47
    return cents


def convert_cents_acer(cents):
    acer = cents / 100
    return acer


if __name__ == "__main__":
    # create_area_file()
    is_patta = True
    is_fmb = True
    if is_fmb:
        is_patta = False
    get_patta_fmb(is_patta)
