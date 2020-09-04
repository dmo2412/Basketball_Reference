from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import requests
import shutil
from xlsxwriter import Workbook
import xlsxwriter as xw

class App:
    def __init__(self, path='/Users/dannymorgan/Desktop/Masters_stats', email='', password=''):
        if not os.path.exists(path):
            os.mkdir(path)

        self.path = path 
        self.email = email
        self.password = password
        self.years = [str(i) for i in range(2010,2020)]
        # self.years = self.years.reverse()
        self.first_url = "https://www.golfstats.com/search/?box="
        self.second_url = "&tournament=Masters&player=&tour=Majors&submit=go"
        self.real_url = "https://www.golfstats.com/"
        self.driver = webdriver.Chrome('/Users/dannymorgan/Downloads/chromedriver')
        self.driver.get(self.real_url)
        self.workbook = Workbook(os.path.join(self.path, 'test_file5.xlsx'))

        sleep(3)
        self.login()
        sleep(3)
        self.failed_login()
        sleep(1)
        self.go_to_masters()

    def login(self):
        clicker = self.driver.find_element_by_xpath("//a[@class='manage button-green']")
        clicker.click()
        enter_email = self.driver.find_element_by_xpath("//input[@id='user_login']")
        enter_email.send_keys(self.email)
        enter_pass = self.driver.find_element_by_xpath("//input[@id='user_pass']")
        enter_pass.send_keys(self.password)
        remember = self.driver.find_element_by_xpath(
            "//input[@id='rememberme']")
        remember.click()
        sign_in = self.driver.find_element_by_xpath("//input[@id='wp-submit']")
        sign_in.click()

    def failed_login(self):
        try:
            soup = BeautifulSoup(self.driver.page_source, 'lxml')
            nums = soup.find_all('span')
            # print(nums)
            self.driver.find_element_by_xpath("//input[@id='jetpack_protect_answer']")
        except Exception:
            pass
            # print('')

    def go_to_masters(self):
        workbook = xw.Workbook(os.path.join(self.path, 'masters_stats_2010_to_2019.xlsx'))
        worksheet = workbook.add_worksheet()
        # workbook = workbook.add_format({'Bold': True})
        # bold = workbook.add_format({'bold': True})
        i = -1
        x = 1
        self.driver.get(self.first_url + self.years[i] + self.second_url)
        self.select_header(worksheet, workbook)
        while i > -11:
            self.driver.get(self.first_url + self.years[i] + self.second_url)
            i -= 1
        # Iterate over the years here and call functions
            sleep(1)
            self.next_year(worksheet, x)
            sleep(1)
            x += 45
            #Stuck here:
            #   Everything is looping through properly but not printing to the excel file
            #
            #
            #
            # i -= 1
        workbook.close()
    
    def select_header(self, worksheet, workbook):
        # bold = worksheet.add_format({'bold': True})
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        all_stats = soup.find_all('tr')
        i = 0
        stats = all_stats[5]
        # while i < 10:
        #     print(stats[i])
        arr = []
        for stat in stats:
            word= str(stat)
            start = word.find('">') + 2
            end = word.find("</td>") - 4
            
            first = int(start)
            last = int(end)
            arr.append(word[start:end])
        while("" in arr):
            arr.remove("")
        
        # workbook = Workbook(os.path.join(self.path, 'test_file8.xlsx'))
        # worksheet = workbook.add_worksheet()
        
        while i < len(arr):
            worksheet.write(0,i, arr[i])
            i += 1
        
        # worksheet.add_format({'bold': True})
        
        # k = 6
        # while k < 25:
        #     col = 0
        #     for stat in all_stats[k]:
        #         word = str(stat)
        #         if "href" in word:
        #             end = word.find("</a>")
        #             start = word.find("=go") + 5
        #         else:
        #             start = word.find('">') + 2
        #             end = word.find("</td>")
        #         xl = word[start:end]
        #         worksheet.write(row, col, xl)
        #         col += 1
        #     k += 1
        #     row += 1

        # for el in range(8):

        # workbook.close()

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
                # try:
                # self.format_xl(xl, start, end)
                #     if xl.startswith('$'):
                #         xl = xl[1:end]
                # except AttributeError:
                #     pass
                # try:
                #     if xl.startswith('$'):
                #         letters = ""
                #         xl = xl[1:end]
                #         eles = list(map(str, xl))
                #         xl = eles.replace(",", "")
                #         print(xl)
                #         xl = "".join(xl)
                #         # i = 0
                #         # for char in eles:
                #         #     if i != 1 or i != 4:
                #         #         letters += char
                #         #     i += 1 
                #         # print(letters)
                #         xl = float(xl)

                # except AttributeError:
                #     pass
                # self.format_xl(xl, start, end)
                try:
                    if xl.startswith('$'):
                        # print(xl)
                        xl = xl[1:end]
                        # print(xl)
                        eles = list(map(str, xl))
                        # print(eles)
                        # xl = eles.replace(",", "")
                        number = ""
                        for el in eles:
                            if el != ",":
                                number += el
                        # print(number)
                        # xl = "".join(xl)
                        xl = float(number)
                        # print(xl)
                        # print(float(xl))
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
        
        # xl = str(xl)
        # xl = xl.split(" ")
        # word = ""
        # for char in xl:
        #     if char != ",":
        #         word += char
        # # "".join(xl)
        # # word = word.split(" ")
        # nums = [str(i) for i in range(0,10)]
        # # print(nums)
        # letters = ""
        # for char in word:
        #     if char == ",":
        #         pass
        #     else:
        #         letters += char 
        
        # if letters != "":
        #     word = letters

        # for char in word:
        #     if char in nums:
        #         # print(word)
        #         word = float(word)
        #         # print("_______________")
        #         # print(word)
        #         break
            


        return xl

    # def remove_commas(self, word):
    #     letters = ""
    #     eles = list(map(str, word))



        



        
     
    




if __name__ == '__main__':
    app = App()
