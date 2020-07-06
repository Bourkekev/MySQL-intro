import os
import datetime
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
        row = ("Bob", 30, "1990-02-06 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES(%s, %s, %s);", row)
        connection.commit()
finally:
    # close the connection, regardless of whether was successful or not
    connection.close()
