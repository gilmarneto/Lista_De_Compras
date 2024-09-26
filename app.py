# data inicial: 10/09/24
# data final: 25/09/24
""" vamos desenvolver uma pequena lista de compras, utilizando o flask e bootstrap """

from flask import Flask, render_template, redirect, request, url_for
from class_lista import ListaProdutos

lp = ListaProdutos()

app = Flask(__name__)

# rota principal, responsável pela tela index
@app.route('/')
def index():
    return render_template('index.html', titulo='Lista de Compras', componente=lp.componentes_tela(), lista=lp.exibir_lista())

# rota adiconar produto na lista
@app.route('/adicionar', methods=['POST',])
def adicionar():
    lp.produto = request.form['produto']
    lp.quantidade = request.form['quantidade']
    lp.adicionar_produto()
    return redirect(url_for('index'))

# rota editar produto
@app.route('/editar')
def editar():
    lp.produto_selecionado = request.args.get('produto')
    lp.editar()
    return redirect(url_for('index'))

# rota alteração de quantidade do produto
@app.route('/alterar', methods=['POST',])
def alterar():
    lp.quantidade = request.form['quantidade']
    lp.alterar()
    return redirect(url_for('index'))

# rota alteração de quantidade do produto
@app.route('/excluir')
def excluir():
    lp.produto_selecionado = request.args.get('produto')
    lp.excluir()
    return redirect(url_for('index'))

# rodar aplicação
app.run(debug=True)