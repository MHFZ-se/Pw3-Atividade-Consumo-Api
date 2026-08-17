#projeto do site de filmes e series filmax
from flask import Flask

app = Flask(__name__, template_folder='views')

app.run(debug=True)
    