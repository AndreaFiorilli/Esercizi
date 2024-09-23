from flask import Flask, json, request
import base64


api=Flask("__name__")

cittadini=[["mario","rossi","09/68","MRORSS0968"],["luca","verdi","06/74","LCAVRD0674"],["carlo","bianchi","05/86","CRLBNC0586"]]



@api.route('/post_create', methods=['POST'])
def process_json():
    print("Ricevuta chiamata")
    auth = request.headers.get('Authorization')
    auth = auth[6:]
    security_data = base64.b64decode(auth)
    print(security_data)
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        json1 = request.json
        print(json1)
        cittadini.append(json1)
        response = {"Esito":"ok","Msg":"Dato inserito"}	
        return json.dumps(response)
    else:
        return 'Content-Type not supported!'
"""
@api.route('/get_read', methods=['GET'])
def read_cittadini():
    for i in cittadini():
        print(i)

@api.route('/delete', methods=['DELETE'])
def process_json1():
    print("Ricevuta chiamata")
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        json1 = request.json
        print(json1)
        if json1 in cittadini:
            cittadini.remove(json1)
            response = {"Esito":"ok","Msg":"Dato eliminato"}	
            return json.dumps(response)
    else:
        return 'Content-Type not supported!'
    

api.run(host="0.0.0.0", port=8085)
"""   


