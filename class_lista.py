# data: 17/09/2024

from class_produto import Produto
from class_tela import Tela

class ListaProdutos(Produto, Tela):
    def __init__(self):
        self.lista_produtos = []

    