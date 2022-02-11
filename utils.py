from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DAILY_INFO_FORM = '''
app.dailyInfoForm.sfdrfj = "n";
app.dailyInfoForm.sfczzz = "n";
app.dailyInfoForm.yqzd = "健康";
'''

def gen_bro(root) -> webdriver.Chrome:
    option = webdriver.ChromeOptions()
    option.add_experimental_option('excludeSwitches', ['enable-automation'])

    option_head = Options()
    option_head.add_argument('--headless')
    option_head.add_argument('--no-sandbox')
    option_head.add_argument('--disable-gpu')
    option_head.add_argument('--disable-dev-shm-usage')
    return webdriver.Chrome(root, options=option, chrome_options=option_head)


def mani(bro: webdriver.Chrome):
    windows = bro.window_handles
    bro.switch_to.window(windows[-1])
    sleep(2)

    bro.execute_script(DAILY_INFO_FORM)
    bro.execute_script('app.saveMrtb()')
    sleep(2)
    bro.refresh()
    bro.quit()

    # bro.find_element_by_xpath('//*[@id="pane-daily_info_tab"]/form/div[4]/div/div[2]/label/span[2]').click()
    # bro.find_element_by_xpath('//*[@id="pane-daily_info_tab"]/form/div[9]/div/label[2]/span[2]').click()
    # bro.find_element_by_xpath('//*[@id="pane-daily_info_tab"]/form/div[15]/div/div/div[1]/input').click()
    # bro.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
    # bro.find_element_by_xpath('//*[@id="pane-daily_info_tab"]/form/div[18]/div/button/span').click()