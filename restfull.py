import requests,time,hashlib, json

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(str(hash_string).encode('utf-8')).hexdigest()
    return sha_signature

#variables
servicio = 954
accessKey = "NTJjZDgzMDZkOGUwMjI1"
secretKey = "BJoFtaCOCbV4ltFrNXWjup6sVLUJohUmH3mk6xdI"
date = time.strftime("%Y-%m-%dT%H:%M:00-5:00")
parametro = str(servicio)+ "." + accessKey + "." + secretKey + "." +str(date)
#has = hashlib.sha256(str(parametro).encode('utf-8')).hexdigest()
has = encrypt_string(parametro)
#json
parametros = { 
"accessKey": accessKey,
"idService": servicio,
"dateRequest": date,
"hashString": has
}
url = "http://pre1a.services.pagoefectivo.pe/v1/authorizations"
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(parametros), headers=headers)
# Imprimimos el resultado si el código de estado HTTP es 200 (OK):
print(parametro)
print(has)
print(r.status_code)
print(r.text)

