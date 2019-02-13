import subprocess,time, os, sys

def backup(archivo,ruta,destino,opcion):
    if opcion=='generate':
        fecha=time.strftime("%Y%m%d-%I%M")
        bckp=destino+'/'+archivo+'-'+fecha+'.tgz'
        os.system('cd '+ruta)
        subprocess.call(['tar','-czvf',bckp,'--exclude=*.git','--exclude=*.mysql','--exclude=*.gz','--exclude=*.info',archivo])
    else:
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
        p=destino+'/'+archivo+'-'+year+m+'*'
        os.system('rm -f '+p)

archivo=sys.argv[1]
ruta=sys.argv[2]
destino=sys.argv[3]
opcion=sys.argv[4]
#Ejemplo
#backup('pp.txt','/home/lmayta/Phyton','/home/lmayta')
backup(archivo,ruta,destino,opcion)
