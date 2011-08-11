### Magento Multiple Shops Setup Python Script juli 2011.
##
#

# imports
import os, errno


def main():
	path = '/home/troels/Git/MagentoMultiShopPy/shops/'
	path = path + 'shopnavn'
	mkdir(path)
	
	# echo .htaccess
	htaccesscode = "hallo du der"
	htaccess = path + '/.htaccess'
	write_file(htaccess, htaccesscode)
	
	# echo index.php
	indexphpcode = "hallo du der"
	indexphp = path + '/index.php'
	write_file(indexphp, indexphpcode)
		

#functions
def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise

def write_file(filename, filecode):
    newfile = open(filename, "w")
    newfile.write(filecode)
    newfile.close()

#def get_code_from_file

# Database Connection Using mysql.connector
# https://launchpad.net/myconnpy

#import mysql.connector
#conn = mysql.connector.Connect(host='127.0.0.1',user='connector',password='connector',database='connector')
#c = conn.cursor()

# sql oprettelse af shops og såvidere

# opret website
#c.execute("""INSERT INTO core_website values (NULL , "websitetest", "websitetest", '0', '0', '0')""")
# printe website_id også og bruge det i næste skridt

# opret store                                               her website_id  navn  Root   Den her skal opdateres
#c.execute("""INSERT INTO core_store_group values (NULL , '0', 'storetest', '3', '0')""") 

# opret storeview 
#c.execute("""INSERT INTO core_store values ()""") 

# print default_store_id og opdaterer sidsti rubrik
#c.execute("""INSERT INTO core_store_group values (VALUES (NULL , '0', 'storetest', '3', '0')""") 

#conn.commit()


if __name__ == "__main__":
    main()

