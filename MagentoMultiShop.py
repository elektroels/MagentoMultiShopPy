### Magento Multiple Shops Python Script juli 2011 by Troels Henningsen. 
##
#

### Possible to do's
##
# function for retrieving configuration options from a file
# import sql statements from a file
# possible to enter db connection parameters along rest of configuration stuff

# imports
import os, errno, mysql.connector, re
from indexphp import indexphp
from htaccess import htaccess

# configuration
magento_path = '/opt/lampp/htdocs/mc01/shops/'
websitename = "websitetest"             # also used as websitecode
storename = "storetest"                 
storeviewname = "storeviewtest"
catalognr = "3"                         # 3 is standard Root Catalog

# sql statements
insert_website = "INSERT INTO core_website values (NULL , '%s', '%s', '0', '0', '0')"
select_websiteid = "select website_id from core_website where name='%s'"
update_groupid = "UPDATE core_website SET default_group_id='%s' WHERE website_id='%s'"
insert_store = "INSERT INTO core_store_group values ('%s' , '%s', '%s', '%s', '0')"
insert_store_view = "INSERT INTO core_store values (NULL, '%s', '%s', '%s', '%s', '0', '1')"
select_storeid = "select store_id from core_store where website_id='%s'"
update_store = "UPDATE core_store_group SET default_store_id='%s' WHERE website_id='%s'"
#insert_coreconfig = "insert into core_config_data values ()"


def main():
        # make directories                                      # http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
        global path
        path = magento_path + websitename
        mkdir(path)

        #mysql_connection()
        mysql_connection()
        
        # echo .htaccess
        write_file('.htaccess', htaccess)
        
        # echo index.php
        write_file('index.php', indexphp % (websitename))
                

#functions
def mkdir(path):
        try:
                os.makedirs(path)
        except OSError as exc: # Python >2.5
                if exc.errno == errno.EEXIST:
                        pass
                else: raise

def write_file(filename, filecode):
        path_file = path + '/' + filename
        newfile = open(path_file, "w")
        newfile.write(filecode)
        newfile.close()

def mysql_connection():
        # Database Connection using mysql.connector module      # https://launchpad.net/myconnpy
        conn = mysql.connector.Connect(host='127.0.0.1', user='mc01', password='thebeginning', database='mc01') # hvordan gør jeg de her parametre dynamiske?!
        c = conn.cursor()

        c.execute(insert_website % (websitename, websitename))
        conn.commit()
        
        # fetch website_id
        c.execute(select_websiteid % (websitename))
        # cleanup id                                            # http://stackoverflow.com/questions/3621296/python-cleaning-up-a-string
        for row in c:
                rx = re.compile('\W+')
                websiteid = rx.sub('', str(row)).strip()

        # update group id
        c.execute(update_groupid % (websiteid, websiteid))
        # create store
        c.execute( insert_store % (websiteid, websiteid, storename, catalognr))
        # create storeview 
        c.execute(insert_store_view % (websitename, websiteid, websiteid, storeviewname))
        conn.commit()
        
        # fetch store_view_id
        c.execute(select_storeid % (websiteid))
        for row in c:
                rx = re.compile('\W+')
                storeid = rx.sub('', str(row)).strip()
        
        # update store with store_view_id
        c.execute(update_store % (storeid, websiteid)) 
        conn.commit()

        # create core_config_data
        #c.execute(insert_coreconfig % ())
        #c.execute(insert_coreconfig % ())
        #c.execute(insert_coreconfig % ())
        #c.execute(insert_coreconfig % ())
        #c.execute(insert_coreconfig % ())
        #c.execute(insert_coreconfig % ())
        
        c.close()


if __name__ == "__main__":
    main()

