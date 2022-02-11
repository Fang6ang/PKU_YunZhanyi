from utils import mani, gen_bro
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os

url = 'https://portal.pku.edu.cn/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
webdvr_url = 'https://registry.npmmirror.com/-/binary/chromedriver/98.0.4758.80/chromedriver_linux64.zip'

# account = {
#     'id': 'xxx',
#     'pass': 'xxx'
# }


def main(dvr_root=r'./chromedriver'):
    bro = gen_bro(root=dvr_root)
    bro.get(url)

    # Loggin portal
    sleep(2)
    try:
        bro.find_element_by_xpath('//*[@id="ng-app"]/div[1]/header/section/section[1]/section[2]/ul[1]/li/a').click()
        print('clicked')
    except NoSuchElementException: # The page's been auto relocated
        sleep(2)
    sleep(2)
    id_input = bro.find_element_by_id('user_name')
    id_input.send_keys(os.environ['ID'])
    pass_input = bro.find_element_by_id('password')
    pass_input.send_keys(os.environ['PASS'])
    bro.find_element_by_id('logon_button').click()
    sleep(3)
    print(f'Log in with ID: {os.environ["ID"]}')

    # try:
    #     btn = bro.find_element_by_xpath('//*[@id="bizTip"]/div/div/div[1]/div/div/table/tbody/tr[11]/td/a')
    #     print('Here')
    #     btn.click()
    #     print('click')
    # except NoSuchElementException:
    #     pass

    bro.refresh()
    sleep(3)
    all_btn = bro.find_element_by_id('all')
    bro.execute_script('arguments[0].click();', all_btn)
    sleep(1)
    bro.find_element_by_id('fav_epidemic').click()
    sleep(10)
    mani(bro)


if __name__ == '__main__':

    chromedriver = "/usr/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    main(chromedriver)