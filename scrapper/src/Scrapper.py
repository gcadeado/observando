import os
import time
import datetime
import Indexer
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import support
from threading import Thread


class scrapper(Thread):

    def __init__(self, driver_path, options, action_queue):
        Thread.__init__(self)
        self.driver = webdriver.Chrome(executable_path=driver_path, options=options)
        self.executable_path = driver_path
        self.options = options
        self.action_queue = [a for a in action_queue]
       
    def run(self):
        for val in self.action_queue:
            eval(val)
        self.scrap()

    #this where the magic happens baby
    def scrap(self):
        try:
            anexo = self.driver.find_element_by_id("ctl00_cphConteudo_frmDetalheLicitacao_lnkDownloadEdital")
            print("achei um anexo")
        except:
            print("nao tem anexo")
            pass

        table = self.driver.find_element_by_id("ctl00_cphConteudo_gdvEventosLicitacao_gdvContent")
        
        try:
            contador = 1
            for tr in table.find_elements_by_tag_name("tr")[1:]:
                link = tr.find_element_by_tag_name("a").get_property("href")
                a = self.action_queue
                a.append("time.sleep(2)")
                s = scrapper(self.driver_path,self.options,["self.driver.get("+link+")", "time.sleep(2)"])
                s.start()
        except:
            pass
        self.driver.close()            
