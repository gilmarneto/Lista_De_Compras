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
        for prod, qtde in self.lista.items():
            print(type(prod))
            print(type(self.produto_selecionado))
            if prod == self.produto_selecionado:
                print('oi')
        



