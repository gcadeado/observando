# TARGET http://e-negocioscidadesp.prefeitura.sp.gov.br/BuscaLicitacao.aspx

import os
import time
import datetime
import Indexer
import Scrapper
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import support
from selenium.webdriver.support.ui import Select

# Intialize the browser

chrome_options = Options()
# chrome_options.add_argument("--headless")
chrome_options.binary_location = '/usr/bin/google-chrome'

driver_path = "/usr/bin/chromedriver"

os.chdir('output')
temp_name = datetime.datetime.fromtimestamp(
    time.time()).strftime('%Y-%m-%d_%H:%M:%S')
os.mkdir(temp_name)
os.chdir(temp_name)

scrap = Scrapper.scrapper(driver_path=driver_path,
                          options=chrome_options, action_queue=[])

indexer = Indexer.indexer(scrap, "http://e-negocioscidadesp.prefeitura.sp.gov.br/BuscaLicitacao.aspx", "", "",
                          "", "", "", "PREGÃO ELETRÔNICO", "ENCERRADA", "", "", "01/01/2000", "18/03/2019", "01/01/2000", "18/03/2019")

indexer.fill_search_page()
indexer.search()

indexer.start_scrapping()
