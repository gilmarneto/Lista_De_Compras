# data: 17/09/2024

from class_produto import Produto
from class_tela import Tela

class ListaProdutos(Produto, Tela):

    def __init__(self):
        super().__init__()
        self.lista = {}

    # MÉTODO ADICIONAR PRODUTOS
    def adicionar_produto(self):
        self.lista[self.produto] = self.quantidade

    # MÉTODO EXIBIR LISTA DE PRODUTOS
    def exibir_lista(self):
        return self.lista
    
    # MÉTODO EDITAR PRODUTO SELECIONADO
    def editar(self):
        self.rota_form = 'alterar'
        self.btn_form = 'Alterar'
        self.disabled_componente = 'disabled'
        for prod, qtde in self.lista.items():
            if prod == self.produto_selecionado:
                self.input_produto = prod
                self.input_quantidade = qtde

    # MÉTODO ALTERAR QUANTIDADE DO PRODUTO 
    def alterar(self):  
        self.lista[self.produto_selecionado] = self.quantidade  
        self.rota_form = 'adicionar'
        self.btn_form = 'Adicionar'
        self.input_produto = ''
        self.disabled_componente = ''
        self.input_quantidade = ''       

    # MÉTODO EXCLUIR PRODUTO 
    def excluir(self):
        del self.lista[self.produto_selecionado]   



