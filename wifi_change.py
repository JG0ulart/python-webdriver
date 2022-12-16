import os, inspect, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from random import randint
from time import sleep

def changer(ipgerencia, nome2g, senha2g, separar_rede):  
    separar_rede = int(separar_rede)
    # Lista de modelos
    acrb = 'HS8546V5'
    acb = 'EG8145V5'
    ax = 'EG8145X6'
    n_model = 'HG8546M'
    acr = ['HS8546V', 'HG8245Q2']
    
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

    browser = webdriver.Chrome(executable_path='/var/kinney-project/python/python-webdriver/chromedriver', chrome_options=chrome_options)
    browser.get(f'https://{ipgerencia}:80')
    titulo1 = browser.title
    print(titulo1)
    # Fase 1
    if titulo1 == "Erro de privacidade":
            advanced = browser.find_element_by_xpath('//*[@id="details-button"]')
            advanced.click()
            go_to = browser.find_element_by_xpath('//*[@id="proceed-link"]')
            go_to.click()
    else:
        print(f"{titulo1}, passou sem advanced")
    onu_model = browser.title
    # AX model
    if onu_model == ax:
        if separar_rede == 1:
                print("Separar redes.")
                user_login = browser.find_element_by_xpath('//*[@id="txt_Username"]')
                pass_login = browser.find_element_by_xpath('//*[@id="txt_Password"]')

                user_login.send_keys("telecomadmin")
                pass_login.send_keys("admintelecom")
                
                login_ONU = browser.find_element_by_id('loginbutton')
                browser.execute_script("arguments[0].click();", login_ONU)
                # login_ONU.click()

                config = browser.find_element_by_xpath('//*[@id="name_addconfig"]')
                config.click()

                wlan = browser.find_element_by_xpath('//*[@id="name_wlanconfig"]')
                wlan.click()

                browser.switch_to.frame('menuIframe')

                name2g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                name2g.clear()
                name2g.send_keys(nome2g)

                pass2g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                pass2g.clear()
                pass2g.send_keys(senha2g)

                apply2g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                apply2g.click()

                browser.save_screenshot(str(randint(1,999))+'image2g.png')
                
                sleep(5)
                print('deu tudo certo até aqui 2g.')

                # 5G
                browser.switch_to.default_content()

                wlan5G = browser.find_element_by_xpath('//*[@id="wlan5basic"]')
                wlan5G.click()

                browser.switch_to.frame('menuIframe')

                name5g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                name5g.clear()
                name5g.send_keys(nome2g+" 5G")

                pass5g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                pass5g.clear()
                pass5g.send_keys(senha2g)

                apply5g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                apply5g.click()

                browser.save_screenshot(str(randint(1,999))+'image5G.png')
                
                sleep(5)
                print('deu tudo certo até aqui 5g.')
                print('ONU finalizada!')

                browser.quit()
                
                return print('deu certo!')
        elif separar_rede == 2:
            print("Não separar redes.")
            user_login = browser.find_element_by_xpath('//*[@id="txt_Username"]')
            pass_login = browser.find_element_by_xpath('//*[@id="txt_Password"]')

            user_login.send_keys("telecomadmin")
            pass_login.send_keys("admintelecom")

            login_ONU = browser.find_element_by_xpath('//*[@id="loginbutton"]')
            browser.execute_script("arguments[0].click();", login_ONU)
            # login_ONU.click()

            config = browser.find_element_by_xpath('//*[@id="name_addconfig"]')
            config.click()

            wlan = browser.find_element_by_xpath('//*[@id="name_wlanconfig"]')
            wlan.click()

            browser.switch_to.frame('menuIframe')

            name2g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
            name2g.clear()
            name2g.send_keys(nome2g)

            pass2g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
            pass2g.clear()
            pass2g.send_keys(senha2g)

            apply2g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
            apply2g.click()

            browser.save_screenshot(str(randint(1,999))+'image2g.png')
            
            sleep(5)
            print('deu tudo certo até aqui 2g.')

            # 5G
            browser.switch_to.default_content()

            wlan5G = browser.find_element_by_xpath('//*[@id="wlan5basic"]')
            wlan5G.click()

            browser.switch_to.frame('menuIframe')

            name5g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
            name5g.clear()
            name5g.send_keys(nome2g)

            pass5g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
            pass5g.clear()
            pass5g.send_keys(senha2g)

            apply5g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
            apply5g.click()

            browser.save_screenshot(str(randint(1,999))+'image5G.png')
            
            sleep(5)
            print('deu tudo certo até aqui 5g.')
            print('ONU finalizada!')

            browser.quit()
            
            return print('deu certo!')
    else:
        try:
            #ONU MODELOS HS8546V5 EG8145V5
            title_bluefirmware = browser.find_element_by_id('welcomtext')
            print(title_bluefirmware)
            if separar_rede == 1:
                print("Separar redes.")
                user_login = browser.find_element_by_xpath('//*[@id="txt_Username"]')
                pass_login = browser.find_element_by_xpath('//*[@id="txt_Password"]')

                user_login.send_keys("telecomadmin")
                pass_login.send_keys("admintelecom")

                login_ONU = browser.find_element_by_xpath('//*[@id="loginbutton"]')
                login_ONU.click()

                config = browser.find_element_by_xpath('//*[@id="name_addconfig"]')
                config.click()

                wlan = browser.find_element_by_xpath('//*[@id="name_wlanconfig"]')
                wlan.click()

                browser.switch_to.frame('menuIframe')

                name2g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                name2g.clear()
                name2g.send_keys(nome2g)

                pass2g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                pass2g.clear()
                pass2g.send_keys(senha2g)

                apply2g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                apply2g.click()

                browser.save_screenshot(str(randint(1,999))+'image2g.png')
                
                sleep(5)
                print('deu tudo certo até aqui 2g.')

                # 5G
                browser.switch_to.default_content()

                wlan5G = browser.find_element_by_xpath('//*[@id="wlan5basic"]')
                wlan5G.click()

                browser.switch_to.frame('menuIframe')

                name5g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                name5g.clear()
                name5g.send_keys(nome2g+" 5G")

                pass5g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                pass5g.clear()
                pass5g.send_keys(senha2g)

                apply5g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                apply5g.click()

                browser.save_screenshot(str(randint(1,999))+'image5G.png')
                
                sleep(5)
                print('deu tudo certo até aqui 5g.')
                print('ONU finalizada!')

                browser.quit()
                
                return print('deu certo!')
            elif separar_rede == 2:
                print("Não separar redes.")
                user_login = browser.find_element_by_xpath('//*[@id="txt_Username"]')
                pass_login = browser.find_element_by_xpath('//*[@id="txt_Password"]')

                user_login.send_keys("telecomadmin")
                pass_login.send_keys("admintelecom")

                login_ONU = browser.find_element_by_xpath('//*[@id="loginbutton"]')
                login_ONU.click()

                config = browser.find_element_by_xpath('//*[@id="name_addconfig"]')
                config.click()

                wlan = browser.find_element_by_xpath('//*[@id="name_wlanconfig"]')
                wlan.click()

                browser.switch_to.frame('menuIframe')

                name2g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                name2g.clear()
                name2g.send_keys(nome2g)

                pass2g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                pass2g.clear()
                pass2g.send_keys(senha2g)

                apply2g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                apply2g.click()

                browser.save_screenshot(str(randint(1,999))+'image2g.png')
                
                sleep(5)
                print('deu tudo certo até aqui 2g.')

                # 5G
                browser.switch_to.default_content()

                wlan5G = browser.find_element_by_xpath('//*[@id="wlan5basic"]')
                wlan5G.click()

                browser.switch_to.frame('menuIframe')

                name5g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                name5g.clear()
                name5g.send_keys(nome2g)

                pass5g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                pass5g.clear()
                pass5g.send_keys(senha2g)

                apply5g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                apply5g.click()

                browser.save_screenshot(str(randint(1,999))+'image5G.png')
                
                sleep(5)
                print('deu tudo certo até aqui 5g.')
                print('ONU finalizada!')

                browser.quit()
                
                return print('deu certo!')
        except:
            if onu_model == n_model:
                # ONU MODELO N
                if separar_rede == 1:
                    browser.quit()
                    return print("ONU não tem rede 5G")
                elif separar_rede == 2:
                    print("ONU modelo N. Somente rede 2.4G")
                    user_login = browser.find_element_by_xpath('//*[@id="txt_Username"]')
                    pass_login = browser.find_element_by_xpath('//*[@id="txt_Password"]')

                    user_login.send_keys("telecomadmin")
                    pass_login.send_keys("admintelecom")

                    login_ONU = browser.find_element_by_xpath('//*[@id="button"]')
                    login_ONU.click()

                    wlan = browser.find_element_by_xpath('//*[@id="headerTab"]/ul/li[5]/div[2]')
                    wlan.click()

                    browser.switch_to.frame('frameContent')

                    name2g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                    name2g.clear()
                    name2g.send_keys(nome2g)

                    pass2g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                    pass2g.clear()
                    pass2g.send_keys(senha2g)

                    apply2g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                    apply2g.click()

                    browser.save_screenshot(str(randint(1,999))+'image2g.png')
                    
                    sleep(5)
                    print('deu tudo certo até aqui 2g.')

                    print('ONU finalizada!')

                    browser.quit()
                    
                    return print('deu certo!')
            else:
                # ONU MODELOS HS8546V HG8245Q2 HS8546V5 FIRMWARE VERMELHA
                if separar_rede == 1:
                    print("Separar redes.")
                    user_login = browser.find_element_by_xpath('//*[@id="txt_Username"]')
                    pass_login = browser.find_element_by_xpath('//*[@id="txt_Password"]')

                    user_login.send_keys("telecomadmin")
                    pass_login.send_keys("admintelecom")

                    login_ONU = browser.find_element_by_xpath('//*[@id="button"]')
                    login_ONU.click()

                    wlan = browser.find_element_by_xpath('//*[@id="headerTab"]/ul/li[5]/div[2]')
                    wlan.click()

                    browser.switch_to.frame('frameContent')

                    name2g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                    name2g.clear()
                    name2g.send_keys(nome2g)

                    pass2g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                    pass2g.clear()
                    pass2g.send_keys(senha2g)

                    apply2g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                    apply2g.click()

                    browser.save_screenshot(str(randint(1,999))+'image2g.png')
                    
                    sleep(5)
                    print('deu tudo certo até aqui 2g.')

                    # 5G
                    browser.switch_to.default_content()

                    wlan5G = browser.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/div')
                    wlan5G.click()

                    browser.switch_to.frame('frameContent')

                    name5g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                    name5g.clear()
                    name5g.send_keys(nome2g+" 5G")

                    pass5g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                    pass5g.clear()
                    pass5g.send_keys(senha2g)

                    apply5g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                    apply5g.click()

                    browser.save_screenshot(str(randint(1,999))+'image5G.png')
                    
                    sleep(5)
                    print('deu tudo certo até aqui 5g.')
                    print('ONU finalizada!')

                    browser.quit()
                    
                    return print('deu certo!')
                elif separar_rede == 2:
                    print("Não separar redes.")
                    user_login = browser.find_element_by_xpath('//*[@id="txt_Username"]')
                    pass_login = browser.find_element_by_xpath('//*[@id="txt_Password"]')

                    user_login.send_keys("telecomadmin")
                    pass_login.send_keys("admintelecom")

                    login_ONU = browser.find_element_by_xpath('//*[@id="button"]')
                    login_ONU.click()

                    wlan = browser.find_element_by_xpath('//*[@id="headerTab"]/ul/li[5]/div[2]')
                    wlan.click()

                    browser.switch_to.frame('frameContent')

                    name2g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                    name2g.clear()
                    name2g.send_keys(nome2g)

                    pass2g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                    pass2g.clear()
                    pass2g.send_keys(senha2g)

                    apply2g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                    apply2g.click()

                    browser.save_screenshot(str(randint(1,999))+'image2g.png')
                    
                    sleep(5)
                    print('deu tudo certo até aqui 2g.')

                    # 5G
                    browser.switch_to.default_content()

                    wlan5G = browser.find_element_by_xpath('//*[@id="nav"]/ul/li[3]/div')
                    wlan5G.click()

                    browser.switch_to.frame('frameContent')

                    name5g = browser.find_element_by_xpath('//*[@id="wlSsid"]')
                    name5g.clear()
                    name5g.send_keys(nome2g)

                    pass5g = browser.find_element_by_xpath('//*[@id="wlWpaPsk"]')
                    pass5g.clear()
                    pass5g.send_keys(senha2g)

                    apply5g = browser.find_element_by_xpath('//*[@id="btnApplySubmit"]')
                    apply5g.click()

                    browser.save_screenshot(str(randint(1,999))+'image5G.png')
                    
                    sleep(5)
                    print('deu tudo certo até aqui 5g.')
                    print('ONU finalizada!')

                    browser.quit()                    
                    return print('deu certo!')
               
#ip = input("Informe o IP: ")
# changer('', "", "", "")