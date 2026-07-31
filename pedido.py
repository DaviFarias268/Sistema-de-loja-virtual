class Pedido:
    def __init__(self, cliente, items_comprados, valor_final):
        self.cliente = cliente
        self.items_comprados = items_comprados
        self.valor_final = valor_final
        self.status = "Pendente"

    def exibir_resumo(self):
        print(f"\n--- RESUMO DO PEDIDO ---")
        print(f"Cliente: {self.cliente.nome}")
        print(f"Total: R${self.valor_final:.2f}")
        print(f"Status: {self.status}")