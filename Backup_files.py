import subprocess,time, os, sys

def backup(archivo,ruta,destino,opcion):
    if opcion=='generate':
        fecha=time.strftime("%Y%m%d-%I%M")
        bckp=destino+'/'+archivo+'-'+fecha+'.tgz'
        os.system('tar -czvf '+bckp+' -C '+ruta+' '+archivo)
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

if archivo=='help':
    print(chr(27)+"[0;33m"+"El script recibe los siquientes parametros: archivo,ruta,destino,opcion[generate,clean]")
    print(chr(27)+"[0;37m"+"generate: crea el backup")
    print('clean: limpia los backups de un mes anterior')
else:
    ruta=sys.argv[2]
    destino=sys.argv[3]
    opcion=sys.argv[4]
    backup(archivo,ruta,destino,opcion)
