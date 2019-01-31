import subprocess,time, os, sys

def limpia(r1,archivo):
    #Limpia Backup
    y=time.strftime("%Y")
    m=time.strftime("%m")
    d=time.strftime("%d")
    # y='2019'
    # m='01'
    # d='19'

    tmp1=int(d) -1
    tmp2="{:02d}".format(tmp1)
    a1=archivo+y+'-'+m+'-'+tmp2
    os.system('gzip '+r1+a1)
    os.system('mv '+r1+'*.gz /ins500/Backup/dspace-cientifico/logs')
def limpiad(r1,archivo,d):
    #Limpia Backup
    # y=time.strftime("%Y")
    # m=time.strftime("%m")
    # d=time.strftime("%d")
    y='2019'
    m='01'

    tmp1=int(d) -1
    tmp2="{:02d}".format(tmp1)
    a1=archivo+y+'-'+m+'-'+tmp2
    print(a1)
    os.system('gzip '+r1+a1)
    os.system('mv '+r1+'*.gz /ins500/Backup/dspace-cientifico/logs')

limpia('/var/lib/docker/volumes/dspace5institucional_dspace/_data/log/','cocoon.log.')
limpia('/var/lib/docker/volumes/dspace5institucional_dspace/_data/log/','dspace.log.')
limpia('/var/lib/docker/volumes/dspace5institucional_dspace/_data/log/','solr.log.')

# for x in range(5,30):
#     i="{:02d}".format(x)
#     limpiad('/var/lib/docker/volumes/dspace5institucional_dspace/_data/log/','cocoon.log.',i)
