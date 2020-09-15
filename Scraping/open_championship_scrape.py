import xlsxwriter as xw
from xlsxwriter import Workbook
import shutil
import requests
import os
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver



class App:
    def __init__(self, path='/Users/dannymorgan/Desktop/Masters_stats', email='', password=''):  #Enter your own email and password and change the path to your destination
        if not os.path.exists(path):
            os.mkdir(path)

        self.path = path
        self.email = email
        self.password = password
        self.years = [str(i) for i in range(2010, 2020)]
        self.first_url = "https://www.golfstats.com/search/?box="
        self.second_url = "&tournament=British+Open&player=&tour=Majors&submit=go"
        self.real_url = "https://www.golfstats.com/"
        self.driver = webdriver.Chrome(
            '/Users/dannymorgan/Downloads/chromedriver')  # Change this path to your own chromedriver path
        self.driver.get(self.real_url)

        sleep(3)
        self.login()
        sleep(3)
        self.go_to_masters()

    def login(self):
        clicker = self.driver.find_element_by_xpath(
            "//a[@class='manage button-green']")
        clicker.click()
        enter_email = self.driver.find_element_by_xpath(
            "//input[@id='user_login']")
        enter_email.send_keys(self.email)
        enter_pass = self.driver.find_element_by_xpath(
            "//input[@id='user_pass']")
        enter_pass.send_keys(self.password)
        remember = self.driver.find_element_by_xpath(
            "//input[@id='rememberme']")
        remember.click()
        sign_in = self.driver.find_element_by_xpath("//input[@id='wp-submit']")
        sign_in.click()

    def go_to_masters(self):
        workbook = xw.Workbook(os.path.join(
            self.path, 'open_championship_stats_2010_to_2019.xlsx'))  # Change this file name to save the file under your desired name
        worksheet = workbook.add_worksheet()
        i = -1
        x = 1
        self.driver.get(self.first_url + self.years[i] + self.second_url)
        self.select_header(worksheet, workbook)
        while i > -11:
            self.driver.get(self.first_url + self.years[i] + self.second_url)
            i -= 1
            sleep(1)
            self.next_year(worksheet, x)
            sleep(1)
            x += 45
        workbook.close()

    def select_header(self, worksheet, workbook):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        all_stats = soup.find_all('tr')
        i = 0
        stats = all_stats[5]
        arr = []
        for stat in stats:
            word = str(stat)
            start = word.find('">') + 2
            end = word.find("</td>") - 4

            arr.append(word[start:end])
        while("" in arr):
            arr.remove("")

        while i < len(arr):
            worksheet.write(0, i, arr[i])
            i += 1
            

    def next_year(self, worksheet, row):
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        all_stats = soup.find_all('tr')

        k = 6
        while k < 51:
            col = 0
            for stat in all_stats[k]:
                word = str(stat)
                if "href" in word:
                    end = word.find("</a>")
                    start = word.find("=go") + 5
                else:
                    start = word.find('">') + 2
                    end = word.find("</td>")
                xl = word[start:end]
                if xl.startswith('T-'):
                    xl = xl[2:end]
                if xl == "E":
                    xl = 0

                try:
                    if xl.startswith('$'):

                        xl = xl[1:end]

                        eles = list(map(str, xl))

                        number = ""
                        for el in eles:
                            if el != ",":
                                number += el

                        xl = float(number)

                except AttributeError:
                    pass

                try:
                    xl = float(xl)
                    worksheet.write_number(row, col, xl)
                except Exception:
                    worksheet.write(row, col, xl)
                col += 1
            k += 1
            row += 1

    def format_xl(self, xl, start, end):
        if xl.startswith('T-'):
            xl = xl[2:end]
        if xl == "E":
            xl = 0
        try:
            if xl.startswith('$'):
                xl = xl[1:end]
                eles = list(map(str, xl))
                xl = eles.replace(",", "")
                xl = "".join(xl)
                print(float(xl))
        except AttributeError:
            pass

        return xl


if __name__ == '__main__':
    app = App()
