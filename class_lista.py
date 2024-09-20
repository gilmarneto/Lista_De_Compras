# data: 17/09/2024

from class_produto import Produto
from class_tela import Tela

class ListaProdutos(Produto, Tela):

    lista = []

    def __init__(self):
        super().__init__()

    # MÉTODO PARA ADICIONAR PRODUTOS
    def adicionar_produto(self):
        pass

    # MÉTODO PARA EXIBIR A LISTA
    @classmethod
    def exibir_lista(cls):
        pass


