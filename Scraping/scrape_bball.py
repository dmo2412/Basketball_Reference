from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import requests
import shutil
from xlsxwriter import Workbook
from fake_useragent import UserAgent


class App:
    def __init__(self, path='/Users/dannymorgan/Desktop/BasketballStats'):
        if not os.path.exists(path):
            os.mkdir(path)

        self.path = path
        self.players = ['Kobe Bryant', 'Michael Jordan', 'Lebron James', 'Carmelo Anthony']  
        self.driver = self.driver = webdriver.Chrome('/Users/dannymorgan/Downloads/chromedriver')
        self.main_url = 'https://www.basketball-reference.com/'
        ua = UserAgent()
        header = {"user-agent": ua.chrome}
        self.driver.get(self.main_url, headers=header)

        sleep(2)
        self.find_player()

    def find_player(self):
        clicker = self.driver.find_element_by_xpath("//input[@class='ac-input completely']")
        clicker.click()
        clicker.send_keys('Kobe Bryant')
        # clicker.submit()
        sleep(1)
        name = self.driver.find_element_by_xpath("//span[@class='search-results-item']")
        name.click()
        sleep(5)
        self.download_stats()

    def download_stats(self):
        soup = BeautifulSoup(self.driver.page_source, 'lxml')
        # all_stats = soup.find_all('td')
        # # print(all_stats)
        # # children = [child for child in all_stats]
        # points = self.driver.find_element_by_xpath(
        #     "//td[@class='right ']")
        # print(points.get_attribute('text'))
        # # print(points.contents)
        # # print(children[-1])
        # for stat in all_stats:
        #     if stat['data-stat'] == 'pts_per_g':
        #         print(stat)
        # table = soup.find_all("table")
        # # tbody = table.find_all('tbody')
        # # th_head = thead.find_all('th')
        # # print(th_head)
        # print(table)
        for script in soup(["script", "style"]):
            script.extract() 
            break   # rip it out


# get text
        text = soup.get_text()

        # break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        # break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)

        print(text)


if __name__ == '__main__':
    app = App()
