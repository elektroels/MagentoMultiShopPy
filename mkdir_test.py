# http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python

import os, errno

def mkdir(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST:
            pass
        else: raise

path = '/opt/lampp/htdocs/mc01/shops/'
navn = 'shopnavn'
path = path + navn
mkdir(path)

