### Magento Multiple Shops Setup Python Script juli 2011.
##
#

# imports
import os, errno
from indexphp import indexphp
from htaccess import htaccess

magento_path = '/home/troels/Git/MagentoMultiShopPy/shops/'
path = magento_path + 'shopnavn'

def main():
        # make directories		# http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
	mkdir(path)

	#mysql_connection()
	
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


if __name__ == "__main__":
    main()

