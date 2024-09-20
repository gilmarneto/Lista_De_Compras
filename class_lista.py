# data: 17/09/2024

from class_produto import Produto
from class_tela import Tela

class ListaProdutos(Produto, Tela):

    def __init__(self):
        super().__init__()
        self.lista = {}

    # MÉTODO PARA ADICIONAR PRODUTOS
    def adicionar_produto(self):
        self.lista = {self.produto:self.quantidade}

    # MÉTODO PARA EXIBIR A LISTA
    def exibir_lista(self):
        for p,q in self.lista.items():
            print(p, " --- ", q)
        return self.lista


