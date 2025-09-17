def intersecao(A, B):
    resultado = []

    for elemento in A:
        if elemento in B:
            if elemento not in resultado:
                resultado.append(elemento)

    return resultado

def entrada_lista(nome_lista):
    lista =[]
    tamanho = int(input(f"Quantos elementos tem na lista {nome_lista} ? "))

    for i in range(tamanho):
        numero = int(input(f"Digite o {i+1}º numero para a lista {nome_lista}: "))
        lista.append(numero)

    return lista

A = entrada_lista("A")
B = entrada_lista("B")

resultado = intersecao(A, B)
print(f"A interseção de A e B é: {resultado}")
