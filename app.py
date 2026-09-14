#projeto do site de filmes e series filmax
from flask import Flask, render_template # é a ferramenta encarregada de renderizar paginas htnl
from controllers import routes
from flask import request 

app = Flask(__name__, template_folder='views')


routes.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
     