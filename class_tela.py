# data: 17/09/2024

class Tela:
    rota_form = 'adicionar'
    btn_form = 'Adicionar'
    input_produto = ''    
    input_quantidade = ''

    def componentes_tela(self):
        self.componentes = {}
        self.componentes['rota_form'] = self.rota_form
        self.componentes['btn_form'] = self.btn_form
        self.componentes['input_produto'] = self.input_produto
        self.componentes['input_quantidade'] = self.input_quantidade
        return self.componentes