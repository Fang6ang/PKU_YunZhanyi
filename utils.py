from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DAILY_INFO_FORM = '''
app.dailyInfoForm.sfdrfj = "n";
app.dailyInfoForm.sfczzz = "n";
app.dailyInfoForm.yqzd = "健康";
app.dailyInfoForm.jrtw = 36.3;
'''

# 所有选项
'''
app.dailyInfoForm.sfhx = "n";                 // 是否返校
app.dailyInfoForm.hxsj = "20200901 120000";   // 返校时间
app.dailyInfoForm.cfdssm = "11";              // 出发地所在省
app.dailyInfoForm.cfddjsm = "01";             // 出发地所在市
app.dailyInfoForm.cfdxjsm = "08";             // 出发地所在区/县
app.dailyInfoForm.dqszdsm = "11";             // 当前所在省
app.dailyInfoForm.dqszddjsm = "01";           // 当前所在市
app.dailyInfoForm.dqszdxjsm = "08";           // 当前所在区/县
app.dailyInfoForm.dqszdgbm = "";              // 当前所在国家
app.dailyInfoForm.dqszdxxdz = "No.5 YHY Rd."; // 当前所在地详细地址
app.dailyInfoForm.sfdrfj = "n";               // 是否当日返京
app.dailyInfoForm.chdfj = "Shin Nippori St."; // 从何地返京
app.dailyInfoForm.sflsss = "n";               // 当日是否留宿宿舍
app.dailyInfoForm.sfcx = "n";                 // 是否出校
app.dailyInfoForm.sfmjqzbl = "n";             // 是否与确诊病例密接
app.dailyInfoForm.sfmjmjz = "n";              // 是否与确诊病例密接者密接
app.dailyInfoForm.hsjcjg = "";                // 核酸检测结果
app.dailyInfoForm.jjgcsj = "";                // 开始居家健康观察的时间
app.dailyInfoForm.sfzgfxdq = "n";             // 是否居住在中高风险地区
app.dailyInfoForm.jrtw = 37;                  // 今日体温
app.dailyInfoForm.sfczzz = "n";               // 是否存在以下症状
app.dailyInfoForm.yqzd = "健康";               // 疫情诊断
app.dailyInfoForm.jqxdgj = "";                // 行动轨迹
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
    sleep(2)
    bro.execute_script('app.saveMrtb()')
    sleep(2)
    bro.refresh()
    bro.quit()

    # bro.find_element_by_xpath('//*[@id="pane-daily_info_tab"]/form/div[4]/div/div[2]/label/span[2]').click()
    # bro.find_element_by_xpath('//*[@id="pane-daily_info_tab"]/form/div[9]/div/label[2]/span[2]').click()
    # bro.find_element_by_xpath('//*[@id="pane-daily_info_tab"]/form/div[15]/div/div/div[1]/input').click()
    # bro.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/ul/li[1]').click()
    # bro.find_element_by_xpath('//*[@id="pane-daily_info_tab"]/form/div[18]/div/button/span').click()