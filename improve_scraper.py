from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep , strftime
from bs4 import Comment
import requests
from bs4 import BeautifulSoup
import pandas as pd
import chromedriver_autoinstaller as chromedriver
import datetime
from enum import Enum
from continuousDates import ContinuousDates

class Cities(Enum):
    Mashhad = 'mashhad'
    
class Scraper:
    city = Cities.Mashhad
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('chromedriver', chrome_options=options)
    
    def timeDateCondition(self, year: int, month: int, day: int, number_of_dates: int) -> pd.DataFrame:
        df_main = pd.DataFrame()
        date_list = []
        time_list = []
        condition_list = []
        list_of_dates = ContinuousDates().createContinousDates(year, month, day, number_of_dates)
        for date in list_of_dates[1]:
            main_year = date.year
            main_month = date.month
            main_day = date.day
            Scraper.driver.get(f'https://www.wunderground.com/history/daily/ir/{Scraper.city}/OIMM/date/{main_year}-{main_month}-{main_day}')
            sleep(10)
            page = BeautifulSoup(Scraper.driver.page_source, "html.parser")
            table = page.find('tbody', {'role':'rowgroup'}) 
            for row in table.find_all('tr', {'class' :'mat-row cdk-row ng-star-inserted'}):  
                for td in row.find_all('td', {'class':'mat-cell cdk-cell cdk-column-dateString mat-column-dateString ng-star-inserted'}):
                    for spn in td.find_all('span', {'class':'ng-star-inserted'}) :
                        time_list.append(spn.string)
                        date_list.append(date)
            for row in table.find_all('tr',{'class' :'mat-row cdk-row ng-star-inserted'}):  
                for td in row.find_all('td',{'class':'mat-cell cdk-cell cdk-column-condition mat-column-condition ng-star-inserted'}):
                    for spn in td.find_all('span', {'class':'ng-star-inserted'}) :
                        condition_list.append(spn.string)
        df_main['Date'] = date_list
        df_main['Time'] = time_list
        df_main['Condition'] = condition_list

        return df_main
