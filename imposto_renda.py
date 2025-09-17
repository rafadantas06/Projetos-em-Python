def calcular_ir(lucro, dias):
    if dias <= 180:
        aliquota = 0.225  
    elif 181 <= dias <= 360:
        aliquota = 0.20  
    elif 361 <= dias <= 720:
        aliquota = 0.175  
    else:
        aliquota = 0.15  
    
    imposto_devido = lucro * aliquota
    
    return imposto_devido

def solicitar_investimento():
    valor_investido = float(input("Informe o valor inicial investido: R$ "))
    valor_final = float(input("Informe o valor final após o período: R$ "))
    dias_investidos = int(input("Informe a quantidade de dias investidos: "))
    
    lucro = valor_final - valor_investido
    
    imposto = calcular_ir(lucro, dias_investidos)
    
    print(f"Lucro obtido: R$ {lucro:.2f}")
    print(f"Imposto de Renda devido: R$ {imposto:.2f}")
    
solicitar_investimento()
    