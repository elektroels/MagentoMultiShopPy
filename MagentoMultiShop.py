### Magento Multiple Shops Setup Python Script juli 2011.

# Database Connection Using mysql.connector
# https://launchpad.net/myconnpy

import mysql.connector

conn = mysql.connector.Connect(host='127.0.0.1',user='connector',password='connector',database='connector')
c = conn.cursor()
#exempel #c.execute("""create table towns (#tid int primary key not NULL ,#name text,#postcode text)""")

# sql oprettelse af shops og såvidere

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
