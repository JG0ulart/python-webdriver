from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from selenium.common.exceptions import NoSuchElementException


def dnschanger(ip_gerencia, primary_dns, secondary_dns):

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--mute-audio')
    chrome_options.headless = True

    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-dev-shm-usage')

    browser = webdriver.Chrome(executable_path='/var/dev-kinney-project/python/python-webdriver/chromedriver', chrome_options=chrome_options)
    # browser.set_window_size(1920, 1080)
    browser.get(f'https://{ip_gerencia}:80')

    #advanced = browser.find_element_by_xpath('//*[@id="details-button"]')
    #advanced.click()
    #go_to = browser.find_element_by_xpath('//*[@id="proceed-link"]')
    #go_to.click()

    user_login = browser.find_element_by_xpath('//*[@id="txt_Username"]')
    pass_login = browser.find_element_by_xpath('//*[@id="txt_Password"]')

    user_login.send_keys("telecomadmin")
    pass_login.send_keys("admintelecom")

    login_ONU = browser.find_element_by_xpath('//*[@id="loginbutton"]')
    login_ONU.click()

    config = browser.find_element_by_xpath('//*[@id="name_addconfig"]')
    config.click()

    lan = browser.find_element_by_xpath('//*[@id="name_lanconfig"]')
    lan.click()

    dhcp = browser.find_element_by_xpath('//*[@id="landhcp"]')
    dhcp.click()

    browser.switch_to.frame('menuIframe')

    pdns = browser.find_element_by_xpath('//*[@id="dnsMainPri"]')
    pdns.clear()
    pdns.send_keys(primary_dns)

    sdns = browser.find_element_by_xpath('//*[@id="dnsMainSec"]')
    sdns.clear()
    sdns.send_keys(secondary_dns)

    applydns = browser.find_element_by_xpath('//*[@id="btnApply_ex"]')
    applydns.click()

    browser.save_screenshot('./image.png')

    sleep(5)
    print('deu tudo certo até aqui.')
    browser.quit()
    
    return print('deu certo!')

ip = input("Say the IP: ")
dnschanger(ip,"8.8.8.8", "4.4.4.4")

