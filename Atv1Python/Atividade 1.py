#Atividade 1
print("Boas vindas, vamos realizar o seu cadastro para te encaminhar para o atendimento")

nome = input("Digite o seu nome:_")
idade = int(input("\n Agora, digite a sua idade:_"))
cidade = input("\n Digite o nome da cidade em que você mora:_")

def chamainformes(nome, cidade, idade):
    print(f"\n Olá, {nome}, parabéns pelos seus {idade} anos de vida, ficamos felizes em saber que você mora em {cidade}")

chamainformes(nome, cidade, idade)

#Atividade 2
contador = 0

def incrementar_Contador(contador):
    mensagem = "contador icrementado"
    contador += 1
    print (mensagem)
    return contador

contador = incrementar_Contador(contador)
print(f"O valor do contador é: {contador}")

#print (mensagem)
#Aqui caso eu tente imprimir a mensagem, o resultado será um erro