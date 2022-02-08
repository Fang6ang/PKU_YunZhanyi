from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def gen_bro(root) -> webdriver.Chrome:
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    option_head = Options()
    option_head.add_argument('--headless')
    option_head.add_argument('--disable-gpu')
    return webdriver.Chrome(root, options=option, chrome_options=option_head)


def mani(bro: webdriver.Chrome):
    pass