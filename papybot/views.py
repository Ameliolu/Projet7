#! /usr/bin/python
# -*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
from flask import jsonify

from .Class_Parser import *
from .Class_Wikimedia import *
from .Class_Maps import *


app = Flask(__name__)

app.config.from_object('config')

GOOGLE_KEY = app.config['GO_KEY']

STOP_WORDS = ['le','la','les', 'Salut', 'GrandPy', '!', '.', 'Est-ce', 'que', 'tu', 'connais', 'l\'adresse', 'd\'', '?', ' ']
 
@app.route('/', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        # print(request.remote_addr) #permet d'obtenir l'adresse du serveur
        # print(request.environ["REMOTE_ADDR"]) #permet d'obtenir l'adresse du client

        data = "vide"
        histoire = "vide"
        adresse = "vide"
        url_carte = "vide"

        for elt in request.values:
            data = elt
        
        #on parse la requête
        data = Parser.supp_espaces(data)
        data = Parser.listage(data)
        data = Parser.filtrage(data, STOP_WORDS)
        print(data)
        data = Parser.final(data)
        
        
        #on tente de récupérer un descriptif wikipedia
        try:
            histoire = Wikimedia.synthese(data)
        except:
            pass
        
        #on tente de récupérer une adresse, et le cas échéant une carte
        try:
            adresse = Maps.get_adresse(data, GOOGLE_KEY)
            url_carte = Maps.get_carte(adresse, GOOGLE_KEY)
        except:
            pass
        
        return jsonify(histoire=histoire, adresse=adresse, url_carte=url_carte)

    return render_template('PapyBot.html')


if __name__ == '__main__':
    app.run(debug=True)