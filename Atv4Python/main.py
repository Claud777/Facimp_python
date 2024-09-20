class Empregado:

    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def __str__(self):
        return f"Empregado: {self.nome}, Salário Base: R${self.salario_base:.2f}"


class Gerente(Empregado):

    def __init__(self, nome, salario_base, bonus_fixo):
        super().__init__(nome, salario_base)
        self.bonus_fixo = bonus_fixo

    def calcular_salario(self):
        return self.salario_base + self.bonus_fixo

    def __str__(self):
        return f"Gerente: {self.nome}, Salário com Bônus: R${self.calcular_salario():.2f}"


class Vendedor(Empregado):

    def __init__(self, nome, salario_base, comissao_percentual, vendas_totais):
        super().__init__(nome, salario_base)
        self.comissao_percentual = comissao_percentual
        self.vendas_totais = vendas_totais

    def calcular_salario(self):
        comissao = (self.comissao_percentual / 100) * self.vendas_totais
        return self.salario_base + comissao

    def __str__(self):
        return f"Vendedor: {self.nome}, Salário com Comissão: R${self.calcular_salario():.2f}"


def criar_gerente():
    nome = input("Digite o nome do gerente: ")
    salario_base = float(input("Digite o salário base do gerente: "))
    bonus_fixo = float(input("Digite o bônus fixo do gerente: "))
    return Gerente(nome, salario_base, bonus_fixo)


def criar_vendedor():
    nome = input("Digite o nome do vendedor: ")
    salario_base = float(input("Digite o salário base do vendedor: "))
    comissao_percentual = float(input("Digite a comissão (em %): "))
    vendas_totais = float(input("Digite o total de vendas: "))
    return Vendedor(nome, salario_base, comissao_percentual, vendas_totais)


def main():
    print("Escolha o tipo de empregado:")
    print("1. Gerente")
    print("2. Vendedor")

    escolha = input("Digite o número correspondente à sua escolha: ")

    if escolha == '1':
        gerente = criar_gerente()
        print(gerente)
    elif escolha == '2':
        vendedor = criar_vendedor()
        print(vendedor)
    else:
        print("Opção inválida!")


if __name__ == "__main__":
    main()
