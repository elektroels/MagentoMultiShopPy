### Magento Multiple Shops Setup Python Script juli 2011.
##
#

#import pyodbc
#dbconn = pyodbc.connect(driver='{SQL Server}', server, database, uid, pwd)

# Database Connection Using mysql.connector
# https://launchpad.net/myconnpy
#

import mysql.connector

conn = mysql.connector.Connect(host='127.0.0.1',user='connector',password='connector',database='connector')
c = conn.cursor()

c.execute("""create table towns (
tid int primary key not NULL ,
name text,
postcode text)""")

# Eget / Eksisterende Produkt katalog
# 
# Manage Stores
# Website Name
# http://1.bp.blogspot.com/-o_G5sn1bct8/TiGWupvb4kI/AAAAAAAAAJo/vpmbaHKG5zE/s1600/05%2Bwebsite%2Binfo.png
# Store Name
# http://3.bp.blogspot.com/-wig9rpuQMVI/TiGXh29gN9I/AAAAAAAAAJ4/RX1PDijpBpc/s1600/07%2Bsave%2Bstore.png
# Store View
# http://1.bp.blogspot.com/-YQ4FZFpR3Uk/TiGYm0jmw3I/AAAAAAAAAKI/mM1W4JbP1zw/s1600/07%2Bsave%2Bstore%2Bview.png
#
# mkdir /shops/<navn>
#
# echo .htaccess
#
# echo index.php
# http://1.bp.blogspot.com/-zv9qS-tDuZc/TiiIu7UTpVI/AAAAAAAAALY/6N4YTrj9ebM/s1600/05%2Bindexphp%2Brun.png
#
# sql Secure og Unsecure URLs
# http://1.bp.blogspot.com/-Pev5Y8ktpJw/TiiFMr_YgwI/AAAAAAAAALQ/nWy7ZyKLQ7Q/s1600/02%2Bshop%2Binfo.png
# http://4.bp.blogspot.com/-NFywHgi_U_U/TiGokm86jiI/AAAAAAAAAKY/RhqYKfW0Oqs/s1600/11%2BREDNING.png
