import requests, os
import json
import mysql.connector

mydb = mysql.connector.connect (
    host="dev-db-utp-inscripcion-admision.c5xivlnip4oj.us-east-2.rds.amazonaws.com",
    user="admin",
    passwd="$DRX2019$",
    database="dev_qcrm"
)
mycursor = mydb.cursor()

mycursor.execute("TRUNCATE TABLE cuenta")

sql = "INSERT INTO cuenta (id_string, codigo_ps, descripcion_crm, naturaleza_id, tipo_cuenta_id, direccion, departamento_id_string, provincia_id_string, distrito_id_string) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
values = []
host = "http://crmdev.utp.edu.pe:8098/api/cuentas/getall"
os.system("curl -X GET "+host+">cuentas.json")

with open('cuentas.json', encoding='utf-8') as file:
    cuentas = json.load(file)
    for cuenta in cuentas:
        val = (
            cuenta["IdAccountCRM"],
            cuenta["CodAccountPS"],
            cuenta["DescAccountCRM"],
            cuenta["IdNaturaleza"],
            cuenta["IdTipoCuenta"],
            cuenta["AccountAddress"],
            cuenta["AccountDepId"],
            cuenta["AccountProvId"],
            cuenta["AccountDistId"]
        )
        values.append(val)
    mycursor.executemany(sql, values)
    mydb.commit()
print("Insert Cuentas Finished", mycursor.rowcount, "was inserted.")
