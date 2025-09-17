import random
#funcionalidades do menu
def cadastro_exercicio():
    nome = input("Digite o exercício a ser cadastrado: ")
    tempo = int(input("Quanto tempo foi gasto no exercício? "))
    calorias = int(input("Quantas calorias foram gastas no exercício? "))
    dia = input("Em qual dia da semana o exercício foi realizado? ").lower()
    cadastro = [nome, tempo, calorias, dia]
    print("Exercício cadastrado com sucesso!")

    return cadastro

def relatorio_diario(dias_semana):
    dia = input("Deseja ver o relatório de qual dia da semana? ").lower()
    calorias = 0
    tempo = 0
 #qual dia é referido
    if dia == "segunda":
        dia_escolhido = dias_semana[0]
    elif dia == "terça" or dia == "terca":
        dia_escolhido = dias_semana[1]
    elif dia == "quarta":
        dia_escolhido = dias_semana[2]
    elif dia == "quinta":
        dia_escolhido = dias_semana[3]
    elif dia == "sexta":
        dia_escolhido = dias_semana[4]
    elif dia == "sábado" or dia == "sabado":
        dia_escolhido = dias_semana[5]
    elif dia == "domingo":
        dia_escolhido = dias_semana[6]
    else:
        print("Dia inválido")

    print("Exercícios realizados: ")
    #exercicios cadastrados no dia escolhido
    if len(dia_escolhido) == 0:
        print("Não há exercícios cadastrados neste dia.")
    else:
        for exercicios in dia_escolhido:
            print(exercicios[0])
            tempo += exercicios[1]
            calorias += exercicios[2]

    print(f"Total de calorias: {calorias} kcal")
    print(f"Tempo gasto no dia: {tempo} minutos")

def calcular_imc():
    peso = float(input("Qual seu peso em quilos? "))
    altura = float(input("Qual sua altura? "))
    imc = peso / (altura**2)
    print("Situação do IMC: ")
    if imc < 18.5:
        print("Magreza")
    elif imc >= 18.5 and imc <= 24.9:
        print("Saudável")
    elif imc >= 25 and imc <= 29.9:
        print("Sobrepeso")
    elif imc >= 30 and imc <= 34.9:
        print("Obesidade grau I")
    elif imc >= 35 and imc <= 39.9:
        print("Obesidade grau II")
    else:
        print("Obesidade grau III")

def meta_semanal(exercicios):
    meta = int(
        input("Qual a meta semanal de calorias que deseja atingir? "))
    gasto_feito = 0
    for exercicio in exercicios:
        gasto_feito += exercicio[2]
    if gasto_feito == meta:
        print("A meta foi alcançada")
    elif gasto_feito > meta:
        print(f"A meta foi superada em {gasto_feito - meta} calorias")
    else:
        print(f"Faltam {meta - gasto_feito} calorias para alcançar a meta")

def frases_motivacionais():
    frases = ["Sem dor, sem ganho.", 
              "Força hoje, resultado amanhã.",
              "Foco, Força, e Fé.",
              "Você é mais forte do que pensa.",
              "Treine duro, brilhe mais.",
              "Menos desculpas, mais ação.",
              "Corpo em movimento, mente em paz."]
    frase_escolhida = random.choice(frases)
    print(frase_escolhida)

def media_calorias(exercicios):
    sum_calorias = 0
    cont = 0
    for i in exercicios:
        sum_calorias += i[2]
        cont += 1
    media = sum_calorias / cont
    print(
        f"A média de calorias gastas por exercício é de {media:.2f} calorias.")

def tabela_calorias(exercicios):
    for exercicio in exercicios:
        print(f"{exercicio[0]} =", end=" ")
        quant_barras = int(exercicio[2] / 10)
        for i in range(quant_barras):
            print("#", end=" ")
        print()

def menu():
    #listas
    resp = 0
    exercicios = []
    segunda = []
    terca = []
    quarta = []
    quinta = []
    sexta = []
    sabado = []
    domingo = []

    while resp != 8:
        print("1. Cadastrar exercício?")
        print("2. Relatório diário?")
        print("3. Calcular IMC?")
        print("4. Meta semanal de calorias?")
        print("5. Alguma frase motivacional?")
        print("6. Média de calorias por exercício?")
        print("7. Tabela de calorias gastas por exercício?")
        print("8. Fechar menu.")
        resp = int(input("Resposta: "))
        dias_semana = [segunda, terca, quarta, quinta, sexta, sabado, domingo]

        if resp == 1:
            exercicio = cadastro_exercicio()
            print()
            exercicios.append(exercicio)
            #exercicios ao dia
            if exercicio[3] == "segunda":
                segunda.append(exercicio)
            elif exercicio[3] == "terça" or exercicio[3] == "terca":
                terca.append(exercicio)
            elif exercicio[3] == "quarta":
                quarta.append(exercicio)
            elif exercicio[3] == "quinta":
                quinta.append(exercicio)
            elif exercicio[3] == "sexta":
                sexta.append(exercicio)
            elif exercicio[3] == "sabado":
                sabado.append(exercicio)
            elif exercicio[3] == "domingo":
                domingo.append(exercicio)

        elif resp == 2:
            if len(exercicios) == 0:
                print("Não há exercícios cadastrados.")
            else:
                relatorio_diario(dias_semana)
                print()
        elif resp == 3:
            calcular_imc()
            print()
        elif resp == 4:
            meta_semanal(exercicios)
            print()
        elif resp == 5:
            frases_motivacionais()
            print()
        elif resp == 6:
            media_calorias(exercicios)
            print()
        elif resp == 7:
            tabela_calorias(exercicios)
            print()
        elif resp == 8:
            print("Obrigado por usar o nosso serviço!")
        else:
            print("Resposta inválida")
menu()
