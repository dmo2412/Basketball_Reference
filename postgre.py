import psycopg2
# conn = psycopg2.connect()
# conn = psycopg2.connect("dbname=tools user=dannymorgan )
# print(pga_test2)
connection = psycopg2.connect(user="dannymorgan",
                              host="127.0.0.1",
                              port="5432",
                              database="test")
cursor = connection.cursor()
postgreSQL_select_Query = "select * from pga_test2"

cursor.execute(postgreSQL_select_Query)
print("Selecting rows from mobile table using cursor.fetchall")
mobile_records = cursor.fetchall()
postgreSQL_select_Query = "select * from pga_test2 where year = 2011"
print(cursor.execute(postgreSQL_select_Query, (id,)))

