from flask import render_template,redirect, url_for
import urllib.request
import json
from flask import request
import random

def init_app(app):
    
    @app.route('/')
    def home():

        urlAPI = 'https://api.tvmaze.com/shows'

        resposta = urllib.request.urlopen(urlAPI)
        dados = resposta.read()

        listaObras = json.loads(dados)

        # Remove obras que não possuem avaliação
        obrasAvaliadas = [
            obra for obra in listaObras
            if obra['rating']['average'] is not None
        ]

        # Ordena da maior avaliação para a menor
        obrasAvaliadas.sort(
            key=lambda obra: obra['rating']['average'],
            reverse=True
        )

        # Pega as 75 mais bem avaliadas
        melhoresObras = obrasAvaliadas[:75]

        # Escolhe 20 aleatoriamente entre as 75
        obrasCarrossel = random.sample(melhoresObras, 20)

        return render_template('index.html',obrasCarrossel=obrasCarrossel)
    
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

    @app.route('/infos/<int:obraid>')
    def infos(obraid):

        # Busca os dados da série
        urlAPI = 'https://api.tvmaze.com/shows/'  + str(obraid)

        respostaSerie = urllib.request.urlopen(urlAPI) 
        dados = respostaSerie.read()
        serie = json.loads(dados)

        # Busca os episódios da série
        respostaEpisodios = urllib.request.urlopen(urlAPI + '/episodes') 
        dadosEpisodeos = respostaEpisodios.read()
        episodios = json.loads(dadosEpisodeos)

        # Quantidade de episódios
        quantidadeEpisodios = len(episodios)

        # Guarda os números das temporadas
        respostaTemporadas = urllib.request.urlopen(urlAPI + '/seasons') 
        dadosTemporadas = respostaTemporadas.read()
        temporadas = json.loads(dadosTemporadas)

        # Quantidade de temporadas
        quantidadeTemporadas = len(temporadas)

        return render_template( 'informacoes.html', serie=serie, quantidadeEpisodios=quantidadeEpisodios, quantidadeTemporadas=quantidadeTemporadas )



    