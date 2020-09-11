from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import requests
import shutil
from xlsxwriter import Workbook
import xlsxwriter as xw


class App:
    def __init__(self, path='/Users/dannymorgan/Desktop/Masters_stats'):
        self.path = path
        self.years = [str(i) for i in range(2019, 2009, -1)]
        self.first_url = "https://www.pgatour.com/content/pgatour/stats/stat.102.y"
        self.second_url = ".html"
        self.driver = webdriver.Chrome(
            '/Users/dannymorgan/Downloads/chromedriver')
        self.workbook = xw.Workbook(os.path.join(
            self.path, 'drive_accuracy_stats_2010_to_2019.xlsx'))
        sleep(3)
        self.next_year()
        self.workbook.close()
        # https://www.pgatour.com/content/pgatour/stats/stat.130.y2019.html
        # https://www.pgatour.com/content/pgatour/stats/stat.104.y2019.html

    def scrape(self, year):
        worksheet = self.workbook.add_worksheet(year)
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        odd_stats = soup.find_all('td')
        even_stats = soup.find_all('tr', class_="")

        i = 3
        row = 0
        col1 = 0
        col2 = 1
        while i < 1000:
            # print(i)
            # print(odd_stats[i])
            # print(" ")
            # print("_____________")
            # i += 7
            rank = odd_stats[i]
            word1 = str(rank)
            rank_start = word1.find('">') + 2
            rank_end = word1.find('</td')
            ranking = word1[rank_start:rank_end]
            ranked = ranking.split()
            rez = ""
            nums = [str(num) for num in range(0, 10)]
            for ele in ranked:
                for char in ele:
                    if char != 'T':
                        rez += char
            final_rank = int(rez)

            name = odd_stats[i + 2]
            word2 = str(name)
            name_start = word2.find('l">') + 3
            name_end = word2.find('</a>')
            final_name = word2[name_start:name_end]
            print(final_name + " : " + str(final_rank))
            i += 7
            worksheet.write(row, col1, final_name)
            worksheet.write_number(row, col2, final_rank)
            row += 1

    def next_year(self):
        for i in self.years:
            string = "fairways_hit_" + i
            self.driver.get(self.first_url + i + self.second_url)
            sleep(4)
            self.scrape(string)
            # break
            sleep(3)


if __name__ == '__main__':
    app = App()
