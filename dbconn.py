# Database Connection Using mysql.connector
# https://launchpad.net/myconnpy

import mysql.connector

def mysql_connection():
        # connect to db
        conn = mysql.connector.Connect(host='127.0.0.1',user='connector',password='connector',database='connector')
        c = conn.cursor()

        # insert website info
        c.execute("""INSERT INTO core_website values (NULL , "websitetest", "websitetest", '0', '0', '0')""")
        conn.commit()

        # fetch website_id 
        c.execute ("""select website_id from core_website where name='websitetest'""")

        # use website id
        for row in c:
                print(row)
                
        # create store                                  her website_id  navn     Root  Den her skal opdateres
        #c.execute("""INSERT INTO core_store_group values (NULL , '0', 'storetest', '3', '0')""") 
        #conn.commit()
        # opret storeview 
        #c.execute("""INSERT INTO core_store values ()""") 
        # print default_store_id og opdaterer sidste rubrik
        #c.execute("""INSERT INTO core_store_group values (VALUES (NULL , '0', 'storetest', '3', '0')""") 
        c.close()

mysql_connection()
