import os

BASEDIR = os.path.dirname(os.path.abspath(__file__))
listdir = os.listdir(BASEDIR)

try :
    os.remove('db.sqlite3')
    print '[-] Remove db.sqlite3'
except :
    None


for curdir in listdir :
    try :
        os.chdir(os.path.join(BASEDIR, curdir, 'migrations'))
        print '[+] Change dir {}/{}'.format(curdir, 'migrations')
        listfile = os.listdir('.')
        # print listfile
        for i in listfile :
            if i != '__init__.py' :
                os.remove(i)
                print '\t[-] Remove {0}'.format(i)
        
        os.chdir(BASEDIR)

    except :
        os.chdir(BASEDIR)