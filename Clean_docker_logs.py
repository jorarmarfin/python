import subprocess, os, sys

contenedores=subprocess.check_output("ls /home/lmayta/Phyton/docker", shell=True)

print(contenedores)

