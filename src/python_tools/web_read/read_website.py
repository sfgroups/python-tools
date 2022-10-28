import requests, lxml
from bs4 import BeautifulSoup
import time
from selenium import webdriver


def Bot():
    pass
    # import Keysbot = webdriver.Chrome("chromedriver.exe")
    # bot.get('http://www.google.com')
    # search = bot.find_element_by_name('q')
    # search.send_keys("@codedev101")
    # search.send_keys(Keys.RETURN)
    # time.sleep(5)
    # bot.quit()

def DoIt():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }

    html = requests.get("https://www.google.com/search?q=kubernetes", headers=headers)
    soup = BeautifulSoup(html.text, "lxml")

    for result in soup.select(".tF2Cxc"):
        title = result.select_one(".DKV0Md").text
        link = result.select_one(".yuRUbf a")["href"]
        displayed_link = result.select_one(".lEBKkf span").text
        snippet = result.select_one(".lEBKkf span").text

        print(f"{title}\n{link}\n{displayed_link}\n{snippet}\n")

if __name__ == "__main__":
    DoIt()