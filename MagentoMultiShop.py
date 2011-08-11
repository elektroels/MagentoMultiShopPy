### Magento Multiple Shops Setup Python Script juli 2011.

# Database Connection Using mysql.connector
# https://launchpad.net/myconnpy

import mysql.connector

conn = mysql.connector.Connect(host='127.0.0.1',user='connector',password='connector',database='connector')
c = conn.cursor()

# sql oprettelse af shops og såvidere

# opret website
c.execute("""INSERT INTO core_website values (NULL , "websitetest", "websitetest", '0', '0', '0')""")
# printe website_id også og bruge det i næste skridt

# opret store                                               her website_id  navn  Root   Den her skal opdateres
c.execute("""INSERT INTO core_store_group values (NULL , '0', 'storetest', '3', '0')""") 

# opret storeview 
#c.execute("""INSERT INTO core_store values ()""") 

# print default_store_id og opdaterer sidsti rubrik
#c.execute("""INSERT INTO core_store_group values (VALUES (NULL , '0', 'storetest', '3', '0')""") 

conn.commit()

# mkdirs
# http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python

import os, errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise

#path = /opt/lampp/htdocs/mc01
#path = path + shopnavn
#mkdir_p(path)

# echo .htaccess	

# echo index.php
# http://1.bp.blogspot.com/-zv9qS-tDuZc/TiiIu7UTpVI/AAAAAAAAALY/6N4YTrj9ebM/s1600/05%2Bindexphp%2Brun.png
