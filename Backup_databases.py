import subprocess,time, os, sys

fecha=time.strftime("%Y%m%d-%I%M")
archivo = fecha+'.sql'
###############DATABASE#############################
database=sys.argv[1]
user=sys.argv[2]
password=sys.argv[3]
carpeta_backup='/home/lmayta'
####################################################
archivo=database+'-'+archivo
dump='mysqldump -u'+user+' -p'+password+' '+database+'>'+archivo
os.system(dump)

#Comprimir
#usando libreria subprocess
subprocess.call(['gzip',archivo])

#Moviendo
subprocess.call(['mv',archivo+'.gz',carpeta_backup])


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
p=database+'-'+year+m+'*'

os.system('rm -f '+p)

# --all-databases par ahacer backups de todos