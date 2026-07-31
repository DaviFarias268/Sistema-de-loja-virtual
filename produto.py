# 🛒 Gerenciamento de produtos
class Produtos:
    def __init__(self, produto, preco, quantidade, codigo):
        self.produto = produto
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def para_dict(self):
        """Converte o objeto para dicionário (necessário para o JSON)."""
        return {
            "produto": self.produto,
            "preco": self.preco,
            "quantidade": self.quantidade,
            "codigo": self.codigo
        }

    def __str__(self):
        return f"Produto: {self.produto} | Quantidade: {self.quantidade} | Preço: R${self.preco:.2f} | Código: {self.codigo}"