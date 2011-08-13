# Database Connection Using mysql.connector
# https://launchpad.net/myconnpy

import mysql.connector
import re

# konfiguration
#hoststr = "host='%s'" #usrstr = "user='%s'" #pwdstr = "password='%s'" #dbstr = "database='%s'"
#host = "127.0.0.1" #user = "connector" #password = "connector" #database = "connector"

websitename = "websitetest" # bliver også brugt som websitecode
storename = "storetest"
storeviewname = "storeviewtest"
catalognr = "3"                 # 3 is standard Root Catalog

# statements
insert_website = "INSERT INTO core_website values (NULL , '%s', '%s', '0', '0', '0')"
select_websiteid = "select website_id from core_website where name='%s'"
insert_store = "INSERT INTO core_store_group values ('%s' , '%s', '%s', '%s', '0')"
insert_store_view = "INSERT INTO core_store values (NULL, '%s', '%s', '%s', '%s', '0', '1')"
select_storeid ="select store_id from core_store where website_id='%s'"
#update_store =""


def mysql_connection():
        # connect to db
        #print(hoststr % (host), usrstr % (user), pwdstr % (password), dbstr % (database))
        conn = mysql.connector.Connect(host='127.0.0.1', user='connector', password='connector', database='connector') # hvordan gør jeg de her parametre dynamiske?!
        c = conn.cursor()

        c.execute(insert_website % (websitename, websitename))
        conn.commit()
        
        # fetch website_id
        c.execute(select_websiteid % (websitename))
        
        # cleanup id		# http://stackoverflow.com/questions/3621296/python-cleaning-up-a-string
        for row in c:
                rx = re.compile('\W+')
                websiteid = rx.sub('', str(row)).strip()

        # create store
        c.execute( insert_store % (websiteid, websiteid, storename, catalognr))
        conn.commit()
        
        # opret storeview 
        c.execute(insert_store_view % (websitename, websiteid, websiteid, storeviewname))
        conn.commit()
        
        # fetch store_view_id
        c.execute(select_storeid % (websiteid))
        for row in c:
                rx = re.compile('\W+')
                storeid = rx.sub('', str(row)).strip()
        
        # update store with store_view_id
        #c.execute(update_store) 

        c.close()

mysql_connection()
