from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time
import re

class Taxovichkof(object):

    def __init__(self, start, finish):

        self.start = re.split(' ', start)
        self.finish = re.split(' ', finish)

    def whoami(self):
        return type(self).__name__

    def checklist(driver):
        
        c = 1
        while c:
            try:
                elem = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="address__suggestions-list"]/ul/li[1]/a | //div[@class="address__suggestions-list"]/ul/li/a')))
                elem.click()
                c = 0
            except Exception as inst:
                print('check failed')
                print(type(inst))    # the exception instance
                print(inst)
                print(inst.args)
                #driver.quit()
                pass
    
        
    
    def crawl(self):

        #try:
        if True:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--window-size=1420,1080')
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            
            t = 1
            while t:
                try:
                    driver = webdriver.Chrome(chrome_options=chrome_options)
                    driver.get('https://taxovichkof.ru/')
                    elem = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'street-0')))
                    elem.send_keys(self.start[0])
                    t = 0
                except Exception as inst:
                    print(type(i))
                    print('tx/n')
                    driver.quit()
                    pass
                    
            
            Taxovichkof.checklist(driver)
            
            t = 1
            while t:
                try:
                    elem = driver.find_element_by_id('building-0')
                    elem.send_keys(self.start[1])
                    t = 0
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst)
                    print(inst.args)
                    #driver.quit()
                    print('none of building-0')
                    pass
            
            
            Taxovichkof.checklist(driver)
            
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
                    t = 0
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst)
                    print(inst.args)
                    #driver.quit()
                    print('none of street-1')
                    pass

            Taxovichkof.checklist(driver)
            
            t = 1
            while t:
                try:
                    elem = driver.find_element_by_id('building-1')
                    elem.send_keys(self.finish[1])
                    t = 0
                except Exception as inst:
                    print(type(inst))    # the exception instance
                    print(inst)
                    print(inst.args)
                    #driver.quit()
                    print('none of building-1')
                    pass
            
            Taxovichkof.checklist(driver)

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
            

            price = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@class="car__price"]'))).text
            price = re.split('\s', price)[0] 

            #price = True
            driver.quit()
            return price

        else:
        #except Exception as inst:
            print(type(inst))    # the exception instance
            print(inst)
            print(inst.args)
            driver.quit()
            return 'crawl err full'
        
def main():
    
    toff = Taxovichkof(start='Революции 33к4', finish='Ленсовета 50к1')
    print(Taxovichkof.crawl(toff))


if __name__ == '__main__':
    main()
