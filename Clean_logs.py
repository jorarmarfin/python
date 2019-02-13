import subprocess,time, os, sys

def limpia(r1,archivo,r2,ext,fecha):
    if fecha==1:
        #Limpia Backup
        y=time.strftime("%Y")
        m=time.strftime("%m")
        d=time.strftime("%d")
        tmp1=int(d) -1
        tmp2="{:02d}".format(tmp1)
        a1=archivo+y+'-'+m+'-'+tmp2+ext
    else:
        a1=archivo+ext

    
    os.system('mv '+r1+'*.gz '+r2)

def limpiad(r1,archivo,ext,r2,y,m,d,g2):
    #Limpia Backup
    for x in range(d,g2):
        tmp2="{:02d}".format(x)
        a1=archivo+y+'-'+m+'-'+tmp2+ext
        os.system('gzip '+r1+a1)
        os.system('mv '+r1+'*.gz '+r2)
#Ejemplo
#limpia('/home/lmayta/Phyton/','pp','/home/lmayta/','.txt',0)
#Ejemplo
#limpiad('/home/lmayta/Phyton/','pp','.txt','/home/lmayta/','2019','01',5,30)
