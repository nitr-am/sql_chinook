import os
import pymysql

username = os.getenv('C9_USER')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Genre;"
        cursor.execute(sql)
        for row in cursor:
            print(row)
        # result = cursor.fetchall()
        # print(result)

finally:
    # Close the connection, regardless of whether or not the above was successful
    connection.close()