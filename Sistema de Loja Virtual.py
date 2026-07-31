import json
import os
from estoque import Estoque
from cliente import Cliente
from produto import Produtos

ARQUIVO_DADOS = "dados.json"

class SistemaLoja:
    def __init__(self):
        self.estoque = Estoque()
        self.carregar_dados()

    def salvar_dados(self):
        """Salva Clientes e Estoque dentro do arquivo JSON."""
        dados = {
            "clientes": [cliente.para_dict() for cliente in Cliente.banco_clientes.values()],
            "estoque": [prod.para_dict() for prod in self.estoque.produtos]
        }
        with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
        print("Dados salvos com sucesso no JSON!")

    def carregar_dados(self):
        """Carrega os dados gravados no JSON ao iniciar o programa."""
        if not os.path.exists(ARQUIVO_DADOS):
            return

        try:
            with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
                dados = json.load(f)

                # Carregar clientes
                for item in dados.get("clientes", []):
                    c = Cliente(item["nome"], item["email"], item["senha"])
                    Cliente.banco_clientes[c.email] = c

                # Carregar produtos do estoque
                for item in dados.get("estoque", []):
                    p = Produtos(item["produto"], item["preco"], item["quantidade"], item["codigo"])
                    self.estoque.produtos.append(p)

            print("📂 Dados anteriores carregados com sucesso do JSON!")
        except Exception as e:
            print(f"⚠️ Erro ao carregar arquivo de dados: {e}")

    def menu_cliente(self, cliente):
        """Sub-menu acessado após o cliente fazer login."""
        while True:
            print(f"\n--- ÁREA DO CLIENTE: {cliente.nome} ---")
            print("1 - Comprar / Adicionar Produto ao Carrinho")
            print("2 - Ver Meu Carrinho")
            print("3 - Remover Produto do Carrinho")
            print("4 - Deslogar")

            opcao = input("Opção: ").strip()

            if opcao == "1":
                # Lista os produtos do estoque
                self.estoque.listar_produtos()
                if not self.estoque.produtos:
                    continue

                try:
                    cod_prod = int(input("\nDigite o código do produto que deseja adicionar: "))
                    produto_encontrado = self.estoque.buscar_por_codigo(cod_prod)

                    if produto_encontrado:
                        cliente.carrinho.adicionar_produto(produto_encontrado)
                    else:
                        print("Produto não encontrado com esse código!")
                except ValueError:
                    print("Código inválido! Digite apenas números.")

            elif opcao == "2":
                cliente.carrinho.mostrar_carrinho()

            elif opcao == "3":
                cliente.carrinho.remover_produto()

            elif opcao == "4":
                print("Logging out...")
                break
            else:
                print("Opção inválida.")

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    sistema = SistemaLoja()

    while True:
        print("\n" + "="*30)
        print("      SISTEMA PRINCIPAL")
        print("="*30)
        print("1 - Cadastrar Cliente")
        print("2 - Logar Cliente")
        print("3 - Gerenciar Estoque (Admin)")
        print("4 - Sair e Salvar Dados")

        opcao = input("Opção: ").strip()

        if opcao == "1":
            Cliente.cadastro()
        elif opcao == "2":
            cliente_logado = Cliente.logar()
            if cliente_logado:
                # Entra na área exclusiva do cliente logado
                sistema.menu_cliente(cliente_logado)
        elif opcao == "3":
            print("\n--- MENU ESTOQUE (ADMIN) ---")
            print("1 - Cadastrar Produto | 2 - Listar | 3 - Deletar")
            sub_op = input("Opção: ")
            if sub_op == "1":
                sistema.estoque.cadastrar()
            elif sub_op == "2":
                sistema.estoque.listar_produtos()
            elif sub_op == "3":
                sistema.estoque.deletar()
        elif opcao == "4":
            sistema.salvar_dados()
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida.")