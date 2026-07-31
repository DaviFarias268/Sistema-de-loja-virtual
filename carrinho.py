class CarrinhoDecompra:
    def __init__(self):
        self.lista_produtos = []
        self.total = 0.0

    def adicionar_produto(self, produto):
        """Recebe um objeto da classe Produtos e adiciona ao carrinho."""
        self.lista_produtos.append(produto)
        print(f" {produto.produto} adicionado ao carrinho com sucesso!")

    def remover_produto(self):
        if not self.lista_produtos:
            print(" Carrinho vazio!")
            return

        try:
            codigo_produto = int(input("Digite o código do produto a remover: "))
            for produto in self.lista_produtos:
                if produto.codigo == codigo_produto:
                    self.lista_produtos.remove(produto)
                    print(" Produto removido do carrinho!")
                    self.calcular_total()
                    return
            print(" Produto não encontrado no carrinho.")
        except ValueError:
            print("Erro: Digite um código numérico válido.")

    def calcular_total(self):
        self.total = sum(p.preco for p in self.lista_produtos)
        return self.total

    def mostrar_carrinho(self):
        if not self.lista_produtos:
            print("O carrinho está vazio.")
            return
        
        print("\n--- ITENS NO CARRINHO ---")
        for produto in self.lista_produtos:
            print(produto)
        print(f"Total Atual: R${self.calcular_total():.2f}")