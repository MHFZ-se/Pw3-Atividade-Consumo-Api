from flask import render_template,redirect, url_for
import urllib.request
import json
from flask import request

def init_app(app):
    
    @app.route('/', methods=['GET', 'POST'])
    def home():
        
        return render_template('index.html')
    
    @app.route('/series')
    def lista():
        urlAPI = 'https://api.tvmaze.com/shows'
        resposta = urllib.request.urlopen(urlAPI)
        dados = resposta.read()
        #print(dados)
        listaObras = json.loads(dados)
        #retorna a lista inteira com tudo
        

    # ROTA DE LOGOUT
        return render_template('lista.html', listaObras = listaObras)


    @app.route('/infos')
    def infos():
        return render_template('informacoes.html')
    



    