# Database Connection Using mysql.connector
# https://launchpad.net/myconnpy

import mysql.connector

def mysql_connection():
        # connect to db
        conn = mysql.connector.Connect(host='127.0.0.1',user='connector',password='connector',database='connector')
        c = conn.cursor()

        # insert website info
        websitename = 'websitetest'
        insert_website_sql = "INSERT INTO core_website values (NULL , '" + websitename + "', '" + websitename + "', '0', '0', '0')"
        
        c.execute(insert_website_sql)
        conn.commit()

        # fetch website_id

        select_website_id_sql = "select website_id from core_website where name='" + websitename + "'"
        c.execute (select_website_id_sql)

        # use website id and clean it up #igang!!
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
