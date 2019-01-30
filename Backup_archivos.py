import subprocess,time, os

fecha=time.strftime("%Y%m%d-%I%M")
archivo = fecha+'.sql'
###############DATABASE#############################
database='october'
user='root'
password='root'
####################################################
archivo=database+'-'+archivo
dump='mysqldump -u'+user+' -p'+password+' '+database+'>'+archivo
os.system(dump)

#Comprimir
#usando libreria subprocess
subprocess.call(['gzip',archivo])

#Limpia Backup
year=time.strftime("%Y")
month=time.strftime("%m")
if month=='12':
    last_month=12
    year= int(year)-1
    year= str(year)
else:
    last_month= int(month)-1

n="{:02d}".format(last_month)
m= str(n)
p=database+'-'+year+m+'*'

os.system('rm -f '+p)
