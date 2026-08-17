from flask import render_template,redirect, url_for
import urllib.request
import json

def init_app(app):
    
    @app.routes('/')
    def home():
        return render_template('index.html')
    
    @app.routs('/infos')
    def infos():
        return render_template('informacoes.html')