import pandas as pd

class ImportExcelToCSV:
    def __init__(self):
        self.years = [str(i) for i in range(2019, 2009, -1)]

        # self.import_masters()
        # self.import_usopen()
        # self.import_pga()
        # self.import_open_championship()
        # self.import_greens_hit()
        # self.import_putting()
        # self.import_fairways_hit()
        # self.import_scrambling()
        # self.import_driving_distance()
        self.import_masters_odds()

    def import_masters(self):
        self.data_xls = pd.read_excel('masters_stats_2010_to_2019.xlsx', 'Sheet1', index_col=None) #Change file name to match file name in Scraping/masters_scrape.py
        self.data_xls.to_csv('Majors/masters.csv', encoding='utf-8')

    def import_usopen(self):
        self.data_xls = pd.read_excel('us_open_stats_2010_to_2019.xlsx', 'Sheet1', index_col=None) #Change file name to match file name in Scraping/us_open_scrape.py
        self.data_xls.to_csv('Majors/usopen.csv', encoding='utf-8')

    def import_pga(self):
        self.data_xls = pd.read_excel('pga_stats_2010_to_2019.xlsx', 'Sheet1', index_col=None) #Change file name to match file name in Scraping/pga_scrape.py
        self.data_xls.to_csv('Majors/pga.csv', encoding='utf-8')

    def import_open_championship(self):
        self.data_xls = pd.read_excel('open_championship_stats_2010_to_2019.xlsx', 'Sheet1', index_col=None) #Change file name to match file name in Scraping/open_championship_scrape.py
        self.data_xls.to_csv('Majors/openchampionship.csv', encoding='utf-8')
    
    def import_masters_odds(self):
        self.data_xls = pd.read_excel('Excel/masters_odds.xlsx', 'Sheet1', index_col = None, header=None)
        self.data_xls.to_csv('Odds/masters_odds.csv', encoding='utf-8')

    def import_greens_hit(self):
        string = 'greens_hit_'
        for year in self.years:
            self.data_xls = pd.read_excel('greens_hit_stats_2010_to_2019.xlsx', string + year, index_col=None, header=None)
            self.data_xls.to_csv('Greens_Hit/greens_hit_' + year + '.csv', encoding='utf-8')

    def import_putting(self):
        string = 'putting_'
        for year in self.years:
            self.data_xls = pd.read_excel('putting_stats_2010_to_2019.xlsx', string + year, index_col=None, header=None)
            self.data_xls.to_csv('Putting/putts_hit_' + year + '.csv', encoding='utf-8')

    def import_fairways_hit(self):
        string = 'fairways_hit_'
        for year in self.years:
            self.data_xls = pd.read_excel('drive_accuracy_stats_2010_to_2019.xlsx', string + year, index_col=None, header=None)
            self.data_xls.to_csv('Fairways_Hit/fairways_' + year + '.csv', encoding='utf-8')

    def import_scrambling(self):
        string = 'scrambling_'
        for year in self.years:
            self.data_xls = pd.read_excel('scrambling_stats_2010_to_2019.xlsx', string + year, index_col=None, header=None)
            self.data_xls.to_csv('Scrambling/up_and_downs_' + year + '.csv', encoding='utf-8')
            
    def import_driving_distance(self):
        string = 'distance_'
        for year in self.years:
            self.data_xls = pd.read_excel('distance_stats_2010_to_2019.xlsx', string + year, index_col=None, header=None)
            self.data_xls.to_csv('Distance/distance_' + year + '.csv', encoding='utf-8')

if __name__ == '__main__':
    imp = ImportExcelToCSV()
