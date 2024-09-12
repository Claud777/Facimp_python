class Aluno:
    def __init__(self, nome, matricula, curso, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4

    # Get's
    def get_nome(self):
        return self.nome
    def get_matricula(self):
        return self.matricula
    def get_curso(self):
        return self.curso
    def get_nota1(self):
        return self.nota1
    def get_nota2(self):
        return self.nota2
    def get_nota3(self):
        return self.nota3
    def get_nota4(self):
        return self.nota4

    # Set's
    def set_nome(self, nome):
        self.nome = nome
    def set_matricula(self, matricula):
        self.matricula = matricula
    def set_curso(self, curso):
        self.curso = curso
    def set_nota1(self, nota1):
        self.nota1 = nota1
    def set_nota2(self, nota2):
        self.nota2 = nota2
    def set_nota3(self, nota3):
        self.nota3 = nota3
    def set_nota4(self, nota4):
        self.nota4 = nota4

    # Média
    def media(self):
        return (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4

    # Aprovado ou Reprovado
    def aprovado(self):
        return self.media() >= 7
    def reprovado(self):
        return self.media() < 7


# Inputs
nome = input("Digite o nome do aluno: ")
matricula = input("Digite a matrícula do aluno: ")
curso = input("Digite o curso do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

# Cria objeto
aluno = Aluno(nome, matricula, curso, nota1, nota2, nota3, nota4)

# Exibição
print(f"Aluno: {aluno.get_nome()}")
print(f"Média: {aluno.media()}")

# Aprovação
if aluno.aprovado():
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")
