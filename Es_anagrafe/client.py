import json,requests
from requests.auth import HTTPBasicAuth

nome=""
cognome=""
data=""
codfisc=""
username = ""
password = ""

def inserisci_cittadino():
        global nome,cognome,data,codfisc
        nome = input('Inserisci il nome del cittadino: ')
        cognome = input('Inserisci il cognome del cittadino: ')
        data = input('Inserisci la data di nascita del cittadino: ')
        codfisc = input('Inserisci il codice fiscale del cittadino: ')
def inserisci_codfisc():
    global codfisc
    codfisc = input('Inserisci il codice fiscale del cittadino da eliminare: ')

def AcquisisciCredenziali():
    global username,password
    username = input('Inserisci username: ')
    password = input('Inserisci password: ')


scelta = input("Inserisci un'operazione da eseguire tra le sequenti: \ncreate\nread\ndelete\nupdate\ninsert\n")
if scelta=="create":
    api_url = "https://127.0.0.1:8085/post_create"
    inserisci_cittadino()
    cittadino = [nome,cognome,data,codfisc]
    response = requests.post(api_url,json=cittadino,verify=False,auth=HTTPBasicAuth(username,password))
    print(response.json())
    print(response.status_code)
    print(response.headers["Content-Type"])
"""
elif scelta=="read":
    api_url = "http://127.0.0.1:8085/get_read"
   print()
elif scelta=="delete":
    api_url = "https://127.0.0.1:8085/delete"
    inserisci_codfisc()
    cittadino=[codfisc]
    response = requests.post(api_url,json=cittadino)
    print(response.json())
    print(response.status_code)
    print(response.headers["Content-Type"])
"""
if scelta=="insert":
    AcquisisciCredenziali()