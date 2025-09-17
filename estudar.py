notas = []

def cadastrar_notas():
    nota = float(input("Cadastrar uma nota (0 a 10). Digite -1 para encerrar: "))
    while nota != -1:
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida!")
        nota = float(input("Cadastrar uma nota (0 a 10). Digite -1 para encerrar: "))

def calcular_media():
    if len(notas) > 0:
        soma = sum(notas)
        return soma / len(notas)


def acima_media(media):
    cont = 0
    for nota in notas:
        if nota > media:
            cont = cont + 1
    print("Quantidade de notas acima da média:", cont)

def maior_menor():
    maior = max(notas)
    menor = min(notas)
    print("Maior nota:", maior)
    print("Menor nota:", menor)

# Execução do programa
cadastrar_notas()
media = calcular_media()
print(f"Média das notas: {media:.2f}")
acima_media(media)
maior_menor()
