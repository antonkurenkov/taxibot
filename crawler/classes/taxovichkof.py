from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time
import re
from datetime import datetime

class Taxovichkof(object):

    def __init__(self, start, finish):

        start = re.split(', ', start)
        self.start = re.split(' ', start[1])
        self.start[1] = self.start[1].replace('к', ' к')
        self.start[1] = re.split(' ', self.start[1])

        finish = re.split(', ', finish)
        self.finish = re.split(' ', finish[1])
        self.finish[1] = self.finish[1].replace('к', ' к')
        self.finish[1] = re.split(' ', self.finish[1])
        
    def whoami(self):
        return type(self).__name__

    def checklist(driver, elem):
        
        c = 1
        while c:
            try:
                time.sleep(1)
                elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="address__suggestions-list"]/ul/li[1]/a | //div[@class="address__suggestions-list"]/ul/li/a')))
                time.sleep(1)
                elem.click()
                c = 0
            except Exception as inst:
                print('check failed')
                elem.send_keys(Keys.BACKSPACE)
                
                #print(f'check failed, time used: {str(total)[:7]}')
                print(type(inst))    # the exception instance
                print(inst)
                print(inst.args)
                #driver.quit()
                pass
    
        
    
    def crawl(self):

        try:
        #if True:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1420,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            
            timer = datetime.now()
            
            t = 1
            while t:
                try:
                    driver = webdriver.Chrome(options=chrome_options)
                    #driver = webdriver.Chrome()
                    driver.get('https://taxovichkof.ru/')
                    time.sleep(0.5)
                    elem = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, 'street-0')))
                    elem.send_keys(self.start[0])
                    time.sleep(0.5)
                    t = 0
                except Exception as inst:
                    print(type(inst))
                    print(inst)
                    print('tx/n')
                    end = datetime.now()
                    total = end - timer
                    print(f'now it is: {str(end)[:7]}')
                    print(f'time used: {str(total)[:7]}')
                    if driver:
                        driver.quit()
                    pass
                    
            
            Taxovichkof.checklist(driver, elem)
            
            t = 1
            while t:
                try:
                    elem = driver.find_element_by_id('building-0')
                    if len(self.start[1]) == 1:
                        elem.send_keys(self.start[1])
                    else:
                        elem.send_keys(self.start[1][0])
                        time.sleep(0.5)
                        elem.send_keys(' ')
                        elem.send_keys(self.start[1][1])
                    time.sleep(0.5)
                    t = 0
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst)
                    print(inst.args)
                    #driver.quit()
                    print('none of building-0')
                    pass
            
            
            Taxovichkof.checklist(driver, elem)
            
            t = 1
            while t:
                try:
                    elem = driver.find_element_by_id('entrance-0')
                    elem.send_keys('1', Keys.RETURN)
                    t = 0
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst)
                    print(inst.args)
                    #driver.quit()
                    print('none of entrance-0')
                    pass
            
            t = 1
            while t:
                try:
                    elem = driver.find_element_by_id('street-1')
                    elem.send_keys(self.finish[0])
                    time.sleep(0.5)
                    t = 0
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst)
                    print(inst.args)
                    #driver.quit()
                    print('none of street-1')
                    pass

            Taxovichkof.checklist(driver, elem)
            
            t = 1
            while t:
                try:
                    elem = driver.find_element_by_id('building-1')
                    if len(self.finish[1]) == 1:
                        elem.send_keys(self.finish[1])
                    else:
                        elem.send_keys(self.finish[1][0])
                        time.sleep(0.5)
                        elem.send_keys(' ')
                        elem.send_keys(self.finish[1][1])
                        
                    time.sleep(0.5)
                    t = 0
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst)
                    print(inst.args)
                    #driver.quit()
                    print('none of building-1')
                    pass
            
            Taxovichkof.checklist(driver, elem)

            t = 1
            while t:
                try:
                    elem = driver.find_element_by_id('entrance-1')
                    elem.send_keys('1', Keys.RETURN)
                    t = 0
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst)
                    print(inst.args)
                    #driver.quit()
                    print('none of entrance-1')
                    pass
            

            #price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="car__price"]'))).text
            time.sleep(0.5)
            price = driver.find_element_by_xpath('//div[@class="car__price"]').text
            price = re.split('\s', price)[0] 

            #price = True
            driver.quit()
            return price

        #else:
        except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst)
            print(inst.args)
            driver.quit()
            return 'crawl err full'
        
def main():
    # start = 'Санкт-Петербург Улица, Ленсовета 50к1'
    # finish = 'Санкт-Петербург Улица, Гжатская 22к4'
    toff = Taxovichkof(start='Санкт-Петербург Улица, Ленсовета 50к1', finish='Санкт-Петербург Улица, Гжатская 22к4')
    print(Taxovichkof.crawl(toff))


if __name__ == '__main__':
    main()
