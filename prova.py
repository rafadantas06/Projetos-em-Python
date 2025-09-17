def calcular(vitorias, empates, derrotas):
    soma = vitorias + empates + derrotas
    return soma / 3

vit = int(input("Quantas vitórias seu time teve: "))
emp = int(input("Quantos empates seu time teve: "))
der = int(input("Quantas derrotas seu time teve:"))

resultado = calcular(vit, emp, der)
print(f"A média de vitórias do seu time foi de: {resultado:.2f}")



      
