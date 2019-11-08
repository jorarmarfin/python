import os
print(chr(27)+"[0;33m"+"Ingresar opcion limpia Cache(lc), Copia archivos files(cf),copia modulos(cm), crear usuarios (cu), elimina usuarios (eu)")
opcion = input()

def lc():
    os.system("docker ps")
def cf():
        return 'cf'
def cm():
        return 'cm'
def cu():
        return 'cu'
def eu():
        return 'eu'
def indirect(i):
        switcher={
                lc:lc,
                cf:cf,
                cm:cm,
                cu:cu,
                eu:eu,
                }
        func=switcher.get(i,lambda :'Invalid')
        return func()

indirect(opcion)
print(f"Me alegro de conocerle, {opcion}")