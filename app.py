# data: 10/09/24
""" vamos desenvolver uma pequena lista de compras, utilizando o flask e bootstrap """

from flask import Flask, render_template, redirect, request, url_for
from class_lista import ListaProdutos

# instância da classe ListaProdutos
lv = ListaProdutos()

app = Flask(__name__)

# rota principal, responsável pela tela index
@app.route('/')
def index():
    return render_template('index.html', titulo='Lista de Compras', produtos=lv.lista_produtos)

# rodar aplicação
app.run(debug=True)