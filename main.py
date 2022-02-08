from utils import mani, gen_bro

url = 'https://portal.pku.edu.cn/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'

account = {
    'id': 'xxx',
    'pass': 'xxx'
}


def main(dvr_root=r'./chromedriver'):
    bro = gen_bro(root=dvr_root)
    bro.get(url)

    # Loggin portal
    id_input = bro.find_element_by_xpath('')
    id_input.send_keys(account['id'])
    pass_input = bro.find_element_by_xpath('')
    pass_input.send_keys(account['pass'])
    log_bttn = bro.find_element_by_xpath('')
    log_bttn.click()

    zhanyi_bttn = bro.find_element_by_xpath('')
    zhanyi_bttn.click()

    mani(bro)


if __name__ == '__main__':
    main()