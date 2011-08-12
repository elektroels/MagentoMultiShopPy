# Database Connection Using mysql.connector
# https://launchpad.net/myconnpy

import mysql.connector
import re

# konfiguration
websitename = "websitetest"
storename = "storetest"
catalognr = "3"                 # 3 is standard Root Catalog

# statements
insert_website = "INSERT INTO core_website values (NULL , '%s', '%s', '0', '0', '0')"
select_websiteid = "select website_id from core_website where name='%s'"
insert_store = "INSERT INTO core_store_group values (NULL , '%s', '%s', '%s', '0')"

#from mystatements import insert_website, select_websiteid
#from myconfig import websitename

def mysql_connection():
        # connect to db
        conn = mysql.connector.Connect(host='127.0.0.1',user='connector',password='connector',database='connector')
        c = conn.cursor()

        c.execute(insert_website % (websitename, websitename))
        conn.commit()
        
        # fetch website_id
        c.execute(select_websiteid % (websitename))
        
        # cleanup id		# http://stackoverflow.com/questions/3621296/python-cleaning-up-a-string
        for row in c:
                rx = re.compile('\W+')
                websiteid = rx.sub('', str(row)).strip()
        #test
        print(websiteid)

        # create store
        c.execute( insert_store % (websiteid, storename, catalognr))
        conn.commit()
        
        # opret storeview 
        #c.execute("""INSERT INTO core_store values ()""") 
        # print default_store_id og opdaterer sidste rubrik
        #c.execute("""INSERT INTO core_store_group values (VALUES (NULL , '0', 'storetest', '3', '0')""") 

        c.close()

mysql_connection()
