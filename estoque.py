from produto import Produtos

class Estoque:
    def __init__(self):
        self.produtos = []

    def buscar_por_codigo(self, codigo):
        """Procura um produto na lista pelo código e o retorna."""
        for produto in self.produtos:
            if produto.codigo == codigo:
                return produto
        return None

    def cadastrar(self):
        try:
            nome_produto = str(input("Digite o nome do produto: ").strip())
            valor_produto = float(input("Digite o valor do produto: ").strip())
            quantidade_produto = int(input("Digite a quantidade do produto: ").strip())
            codigo_produto = int(input("Escreva o código do produto: ").strip())

            cadastro_produto = Produtos(nome_produto, valor_produto, quantidade_produto, codigo_produto)
            self.produtos.append(cadastro_produto)
            print("Produto cadastrado com sucesso!")
        except ValueError:
            print("Erro: Digite apenas números válidos para valor, quantidade e código.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto cadastrado no estoque.")
            return

        print("\n--- LISTA DE PRODUTOS DISPONÍVEIS ---")
        for product in self.produtos:
            print(product)

    def deletar(self):
        if not self.produtos:
            print("Nenhum produto cadastrado para deletar.")
            return

        try:
            codigo_produto = int(input("Digite o código do produto que deseja deletar: ").strip())
            for product in self.produtos:
                if product.codigo == codigo_produto:
                    self.produtos.remove(product)
                    print("Produto deletado com sucesso!")
                    break
            else:
                print("Produto não encontrado.")
        except ValueError:
            print("Erro: Digite um código válido.")