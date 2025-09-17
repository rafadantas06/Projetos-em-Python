valor = float(input("Quanto deseja investir? "))
percentual = int(input("Qual o percentual do CDI? "))
dias = int(input("Qual o período do investimento, em dias? "))

def calcular_cdi(valor_investido, percentual_cdi, dias):
    rendimento = valor_investido * (1+ (percentual_cdi/100)* (dias/252))
    return rendimento

resultado = calcular_cdi(valor, percentual, dias)
print("Seu investimento tera um retorno de: R$", resultado)

if valor > 10000:
    print("Valores acima de R$10000,00 possuem melhor rentabilidade em investimentos privados.")