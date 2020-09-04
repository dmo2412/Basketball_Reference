from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
import os
import requests
import shutil
from xlsxwriter import Workbook

class App:
    def __init__(self, path='/Users/dannymorgan/Desktop/MastersStats', email='djmorgan2412@gmail.com', password='dmo1993'):
        if not os.path.exists(path):
            os.mkdir(path)

        self.path = path 
        self.email = email
        self.password = password
        self.years = [str(i) for i in range(2010,2020)]
        self.first_url = "https://www.golfstats.com/search/?box="
        self.second_url = "&tournament=Masters&player=&tour=Majors&submit=go"
        self.real_url = "https://www.golfstats.com/"
        self.driver = webdriver.Chrome('/Users/dannymorgan/Downloads/chromedriver')
        self.driver.get(self.real_url)

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
        self.driver.get(self.first_url + self.years[0] + self.second_url)
        # Iterate over the years here and call functions
        self.select_header()
    
    def select_header(self):
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
        
        workbook = Workbook(os.path.join(self.path, 'test_file5.xlsx'))
        worksheet = workbook.add_worksheet()
        
        while i < len(arr):
            worksheet.write(0,i, arr[i])
            i += 1
        
        # workbook.close()
        # k = 6
        # while k < 12:
        #     stats = all_stats[k]
        #     array = []
        #     # for stat in stats:
        #     #     word = str(stat)
        #     #     start = word.find('">') + 2
        #     #     end = word.find("</td>") - 4
        #     #     array.append(word[start:end])
        #     # print(array)
        #     print(stats)
        #     k += 1
        # print(all_stats[6])
        k = 6
        row = 1
        while k < 25:
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
                worksheet.write(row, col, xl)
                col += 1
            k += 1
            row += 1
        workbook.close()
        



        
     
    




if __name__ == '__main__':
    app = App()
