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

    def scrap(self):
        pass
