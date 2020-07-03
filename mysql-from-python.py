import os
import pymysql

# Get username from workspace
# modify this variable if running on another environment
username = os.getenv('C9_USER')

# Connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')


try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # close the connection, regardless of whether was successful or not
    connection.close()
