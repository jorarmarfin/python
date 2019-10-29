import subprocess,time, os, sys

v_file = sys.argv[1]
v_limit = sys.argv[2]
v_bytes = v_limit*1024*1024
sizefile = os.stat(v_file).st_size
#1048576000 = 1000 Mb
if sizefile>=v_bytes:
    print(sizefile)
    os.system('cp '+v_file+' '+v_file+'.tmp')
    os.system('true>'+v_file)

