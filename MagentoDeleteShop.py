### Magento Delete Shop Python Script juli 2011 by Troels Henningsen. 
##
#

import mysql.connector, shutil, re

# configuration
magento_path = '/opt/lampp/htdocs/mc01/shops/'                  # path to your shop subfolder in magento dir
websitename = "websitetest"                                     # name of website to be deleted 

# sql statements
select_websiteid = "select website_id from core_website where name='%s'"
delete_data = "DELETE FROM %s WHERE %s = '%s'"

def main():
        # detele folders and files
        delete_ff(magento_path, websitename)
        print("folders deleted")
        
        # delete information in db
        dl_dbdata()
        print("db information deleted")

        print("shop deleted")


#functions
def delete_ff(path, name):
        try:
                path = path + name
                shutil.rmtree(path)
        except:
                print("folder doesn't exist")


def dl_dbdata():
        # Database Connection using mysql.connector module      # https://launchpad.net/myconnpy
        conn = mysql.connector.Connect(host='127.0.0.1', user='mc01', password='thebeginning', database='mc01') # db parameters
        c = conn.cursor()
        
        # fetch website_id
        c.execute(select_websiteid % (websitename))
        # cleanup id                                            # http://stackoverflow.com/questions/3621296/python-cleaning-up-a-string
        for row in c:
                rx = re.compile('\W+')
                websiteid = rx.sub('', str(row)).strip()
                print(websiteid)
        
        # delete data from core_config_data table
        c.execute(delete_data % ("core_config_data", "scope_id", websiteid)) 

        # delete data from core_website table
        c.execute(delete_data % ("core_website", "website_id", websiteid)) 
        
        conn.commit()
        c.close()        


if __name__ == "__main__":
    main()

