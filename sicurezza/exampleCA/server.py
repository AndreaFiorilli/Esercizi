import requests, json, sys
import subprocess
from myjson import *
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
base_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key="
google_api_key = "AIzaSyD7b93nZJudvYnHUVVby9rFWN0h_P49Pgk"

from flask import Flask, render_template, request

api = Flask(__name__)

def ComponiJsonPerImmagine(sImagePath):
  subprocess.run(["rm", "./image.jpg"])
  subprocess.run(["rm", "./request.json"])
  subprocess.run(["cp", sImagePath,"./image.jpg"])
  subprocess.run(["bash", "./creajsonpersf.sh"])

@api.route('/', methods=['GET'])
def index():
    return render_template('sendfile.html')

@api.route('/mansendfile', methods=['POST'])
def mansendfile():
    api_url = base_url + google_api_key
    if not request.files.get("file"):
        mail=request.form['message']
        jsonDataRequest ={"contents":[{"parts":[{"text":mail}]}]}
        #jsonDataRequest["contents"][0]["parts"][0]["text"]=sArgomento
        response=requests.post(api_url,json=jsonDataRequest,verify=False)
        if response.status_code==200:
            dResponse=response.json()
            dListaContenuti=dResponse['candidates'][0]
            sTestoPrimaRisposta=dListaContenuti['content']['parts'][0]['text']
            print(sTestoPrimaRisposta)
            return "<HTML><BODY>DATI RICEVUTI CORRETTAMENTE<br>RISPOSTA:"+ sTestoPrimaRisposta +"<br></BODY></HTML>"
    else:
        f = request.files["file"]
        print("Nome del file " + f.filename)
        f.save("./FileRicevuti/" + f.filename)
        mail=request.form['message']
        ComponiJsonPerImmagine("./FileRicevuti/" + f.filename)
        dJsonRequest=JsonDeserialize("request.json")
        dJsonRequest["contents"][0]["parts"][0]["text"]=mail
        response=requests.post(api_url,json=dJsonRequest,verify=False)
        if response.status_code==200:
            dResponse=response.json()
            dListaContenuti=dResponse['candidates'][0]
            sTestoPrimaRisposta=dListaContenuti['content']['parts'][0]['text']
            print(sTestoPrimaRisposta)
            return "<HTML><BODY>DATI RICEVUTI CORRETTAMENTE<br>RISPOSTA:"+ sTestoPrimaRisposta +"<br></BODY></HTML>"

    

api.run(host="0.0.0.0",port=8085, ssl_context=('./certs/01.pem', './testkey.pem'))
