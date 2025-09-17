def verificar_resgate(valor_inicial, taxa, dias, prazo_minimo):
    taxa_ano = taxa / 100  
    rendimento_ano = valor_inicial * (1 + taxa_ano) * (dias / 365) 

    if dias < prazo_minimo:
        valor_resgate = valor_inicial * 0.95  
        print(f"Resgate antecipado! Penalidade de 5% aplicada. Valor resgatado: R$ {valor_resgate:.2f}")
    else:
        valor_resgate = rendimento_ano
        print(f"Resgate no vencimento. Valor resgatado: R$ {valor_resgate:.2f}")

    if dias < prazo_minimo:
        print("Não vale a pena resgatar antes do prazo mínimo.")
    else:
        print("Vale a pena esperar até o vencimento.")

def solicitar_investimento():
    valor_investido = float(input("Informe o valor investido: R$ "))
    taxa_ano = float(input("Informe a taxa de rentabilidade ao ano (%): "))
    dias_investidos = int(input("Informe a quantidade de dias investidos: "))
    prazo_minimo = int(input("Informe o prazo mínimo em dias: "))
    
    verificar_resgate(valor_investido, taxa_ano, dias_investidos, prazo_minimo)

solicitar_investimento()