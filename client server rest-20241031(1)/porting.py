import os
import dbclient as db
import sys
import json
mydb=db.connect()
if mydb is None:
    print("Error connecting to database")
    sys.exit()
else:
    print("Connected to database")
    db.close(mydb)

cittadini={}
with open("anagrafe.json","r") as json_file:
    cittadini=json.load[json_file]

for key,item in cittadini.items():
    cod_fiscale=key
    nome=item["nome"]
    cognome=item["cognome"]
    data_nascita=item["dataNascita"]
    sQuery="insert into cittadini[codice_fiscale,nome,cognome,data_nascita] values "