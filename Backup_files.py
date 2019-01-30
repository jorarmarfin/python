import subprocess,time, os, sys

sufijo=time.strftime("%Y%m%d-%I%M")
###############CONFIGURACION########################
proyecto=sys.argv[1]
org=sys.argv[2]
bckp=sys.argv[3]
####################################################
archivo=bckp+'/'+proyecto+'-'+sufijo+'.tgz'
#Backup de archivos
subprocess.call(['tar','-czvf',archivo,org])

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
p=bckp+'/'+proyecto+'-'+year+m+'*'
os.system('rm -f '+p)
