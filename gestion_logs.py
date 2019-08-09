import os,sys
# First go to the "/var/www/html" directory
os.chdir("/var/www/html" )

# detect the current working directory
path = os.getcwd()

# read the entries
with os.scandir(path) as listOfEntries:
    for entry in listOfEntries:
        # print all entries that are files
        if entry.is_file():
            sizefile = os.stat(entry.name).st_size
            if sizefile>1073741824:
                comando = 'tail -n 1000 '+entry.name+'> tmp.log && cat tmp.log>'+entry.name+' && rm tmp.log'
                os.system(comando)