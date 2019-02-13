import subprocess,time, os, sys

def backup(database,destino,user,opcion):
    if opcion=='generate':
        fecha=time.strftime("%Y%m%d-%I%M")
        bckp = database+'-'+fecha+'.sql'
        dump='mysqldump -u'+user+' '+database+'>'+bckp
        os.system(dump)
        os.system('gzip '+bckp)
        os.system('mv '+bckp+'.gz'+' '+destino)
    elif opcion=='clean':
        #Limpia Backup
        year=time.strftime("%Y")
        month=time.strftime("%m")
        if month=='01':
            last_month=12
            year= int(year)-1
            year= str(year)
        else:
            last_month= int(month)-1

        n="{:02d}".format(last_month)
        m= str(n)
        p=destino+'/'+database+'-'+year+m+'*'

        os.system('rm -f '+p)
    else:
        print('')

database=sys.argv[1]
if database=='help':
    print(chr(27)+"[0;33m"+"El script recibe los siquientes parametros: database,destino,user,opcion[generate,clean]")
    print(chr(27)+"[0;37m"+"generate: crea el backup")
    print('clean: limpia los backups de un mes anterior')
else:
    destino=sys.argv[2]
    user=sys.argv[3]
    opcion=sys.argv[4]
    backup(database,destino,user,opcion)

# --all-databases par ahacer backups de todos

# GRANT LOCK TABLES, SELECT ON *.* TO 'drinuxbackup'@'%' IDENTIFIED BY '76df9659334938af62378811369fc332';
# [mysqldump]
# user=drinuxbackup
# password=76df9659334938af62378811369fc332