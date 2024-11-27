from flask import Flask, render_template, request


api=Flask("__name__")

utenti=[["mariorossi@gmail.com","abcdefg1234","pippo"],["ciao@gmail.com","totti","mario"]]
utente=[]

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/registrati', methods=['GET'])
def registra():
    utente=[]
    utente.append(request.args.get("email"))
    utente.append(request.args.get("codfisc"))
    utente.append(request.args.get("password"))
    if utente in utenti:
        return render_template('regok.html')
    else:
        return render_template('regko.html')



api.run(host="0.0.0.0", port=8085)
