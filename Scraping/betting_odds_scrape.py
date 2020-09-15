from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import requests
import shutil
from xlsxwriter import Workbook
import xlsxwriter as xw

class App:
    def __init__(self, path='/Users/dannymorgan/Desktop/Masters_stats/Importing/Excel'):
        self.path = path
        self.url = "https://www.sportsoddshistory.com/golf-champs/"
        self.driver = webdriver.Chrome('/Users/dannymorgan/Downloads/chromedriver')
        self.workbook = xw.Workbook(os.path.join(
            self.path, 'masters_odds.xlsx'))
        self.driver.get(self.url)
        self.get_odds()
        self.workbook.close()

    def get_odds(self):
        worksheet = self.workbook.add_worksheet()
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        odds = soup.find_all('td')

        
        i = 0
        arr = []
        while i < 70:
            word = odds[i].text

            if i % 7 != 6:
                arr.append(word)
            i += 1
       
        x = 0 
        row = 0
        nums = [num for num in range(0,6)]
       
        while x < len(arr):
            for num in nums:
                if num != 1:
                    try:
                        ele = float(arr[num + x])
                        worksheet.write_number(row, num, ele)
                    except ValueError:
                        worksheet.write(row, num, 0)
                else:
                    worksheet.write(row, num, arr[num + x])
            x += 6
            row += 1
        



            


    



if __name__ == '__main__':
    app = App()
