# PGA_stat_tracker
PGA_stat_tracker scrapes all of the available information from golfstats.com on all four majors, as well as many relevant stats from pgatour.com,
writes the data to excel, uses pandas to convert the excel file to CSV and add's the CSV to a PostgreSQL database for querying in order to give the clearest
picture of all of the available data.

Tech Stack
* Python - (Selenium, BeautifulSoup, OS, xlsxwriter, pandas)
* PostgreSQL

Webscraping:
  The webscraping files use Selenium webdriver to direct chrome to the desired url. Then uses Beautiful Soup to read the html of golfstats.com and pgatour.com, 
  then iterates over each desired element and writes to it to an excel file. For the majors on golfstats.com, it first scrapes the tournament stats in 2019, then 2018
  all the way down to 2010. For the stats on pgatour.com it first scrapes the 2019 stats and writes it to a worksheet, then does the same for each year in a new 
  worksheet within the same workbook.
  
Importing:
  The importing files use pandas to read the excel files created through scraping, convert them to comma delimited CSV files, and imports them into the Project for 
  use in SQL querying.
  
PostgreSQL:
  The .sql files convert the CSV files into a usable psql database table for querying. Querying is done on multiple tables to show the most relavant statistics 
  for the masters from 2010 through 2019. The output of the most important queries is shown in /SQL/masters_analysis.txt. 
  EG:
    4) Average stats of winners:

    SELECT round(avg(fairways_rank),1) as fairways_hit_rank, round(avg(driving_distance_rank),1) as driving_distance_rank, round(avg(greens_hit_rank),1) as greens_hit_rank, round(avg(putts_rank),1) as putts_rank
    from masters
    where finish = 1;

    fairways_hit_rank | driving_distance_rank | greens_hit_rank | putts_rank 
    -------------------+-----------------------+-----------------+------------
                 29.1 |                  20.3 |             6.3 |       17.9


Instructions to run Webscrape: Hint(For use of golfstats.com, a username and password is required on the site in order to view the complete information)
  1) git clone https://github.com/dmo2412/PGA_stat_tracker
  2) Change path, enter username and email
  3) Change Chromedriver path to your chromedriver path
  4) Terminal: python3 (filename.py)

Instructions to Import and convert to CSV:
  1) Uncomment out method to run in init
  2) Change filename to the name of your excel file.
  3) Enter output location and name for CSV
  4) python3 (filename.py)
  
Instructions for Adding CSV to sql database:
  1) Terminal: cat create_tables.sql | psql (local database name)
  2) Terminal: psql (database_name)
  3) Terminal: \copy table_name from (Path to CSV file) DELIMITER ',' CSV HEADER;

  
  
