from carrinho import CarrinhoDecompra

class Cliente:
    banco_clientes = {}

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.carrinho = CarrinhoDecompra()

    def para_dict(self):
        """Converte o cliente em um dicionário para o JSON."""
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha
        }

    def __str__(self):
        return f"Nome: {self.nome} | E-mail: {self.email}"

    @classmethod
    def cadastro(cls):
        print("\n" + "=" * 20 + "\nCADASTRO DE CLIENTE\n" + "=" * 20)
        email = input("Digite seu e-mail: ").strip()

        if email in cls.banco_clientes:
            print("Erro: Este e-mail já está cadastrado!")
            return None

        nome = input("Digite seu nome: ").strip()
        senha = input("Digite sua senha: ").strip()

        novo_cliente = cls(nome, email, senha)
        cls.banco_clientes[email] = novo_cliente
        print(f"Cadastro efetuado com sucesso! Bem-vindo(a), {nome}!")
        return novo_cliente

    @classmethod
    def logar(cls):
        print("\n" + "=" * 20 + "\nLOGIN DE CLIENTE\n" + "=" * 20)
        email = input("Digite seu e-mail: ").strip()
        senha = input("Digite sua senha: ").strip()

        if email in cls.banco_clientes:
            cliente = cls.banco_clientes[email]
            if cliente.senha == senha:
                print(f" Login efetuado com sucesso! Bem-vindo(a), {cliente.nome}!")
                return cliente
            print(" Senha incorreta!")
        else:
            print(" E-mail não cadastrado!")
        return None