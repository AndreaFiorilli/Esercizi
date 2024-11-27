from flask import Flask, render_template, request
api=Flask("__name__")


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')
@api.route('/mansendfile', methods=['POST'])
def index():
    sMailRicevuta= request.form("email")
    sResponsePage = "<html><body><h1>Buongiorno" + sMailRicevuta + " a tutti, il 17 settembre 2024</h1></body></html>"
    return render_template('index.html')


api.run(host="0.0.0.0", port=8085)
