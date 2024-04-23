class Pedido:
    def __init__(self):
        self.itens = []
        self.total = 0.0
        self.status = "Pendente"
    
    def adicionar_item(self, item, preço):
        self.itens.append((item, preço))
        self.total += preço
    
    def calcular_total(self):
        return self.total
    
    def alterar_status(self, novo_status):
        self.status = novo_status

if __name__ == "__main__":
    pedido1 = Pedido()
    pedido1.adicionar_item("Hambúrguer", 10.99)
    pedido1.adicionar_item("Batata Frita", 4.99)
    pedido1.adicionar_item("Água", 2.49)

    print("Itens do pedido:", pedido1.itens)
    print("Total a ser pago:", pedido1.calcular_total())
    print("Status do pedido:", pedido1.status)

    pedido1.alterar_status("Entregue")
    print("Novo status do pedido:", pedido1.status)
