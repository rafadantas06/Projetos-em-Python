placa = input("Digite sua placa: ")
nome = input("Digite seu nome completo: ")
velocidade = float(input("Velocidade registrada (km/h): "))
vel_max = float(input("Velocidade máxima permitida na via (km/h): "))
reincidencia = input("Você já foi multado anteriormente? (Sim/Não): ")
pagar_imediatamente = input("Deseja pagar a multa imediatamente? (Sim/Não): ")

def infracao(velocidade, vel_max):
    if velocidade <= vel_max:
        return "Sem infração", 0, 0
    elif velocidade <= vel_max * 1.2:
        return "Infração leve", 130.16, 0
    elif velocidade <= vel_max * 1.5:
        return "Infração grave", 195.23, 5
    else:
        return "Infração gravíssima", 880.41, 7
    
def multado(reincidencia, tipo_de_infracao, multa):
    if reincidencia and tipo_de_infracao in ["Infração grave", "Infração gravíssima"]:
        return multa * 2  
    

def curso_reciclagem(tipo_de_infracao):
    if tipo_de_infracao == "Infração gravíssima":
        return "Você precisa fazer um curso de reciclagem no Detran."
    

def simular(multa, pagar_imediatamente):
    if pagar_imediatamente == "sim":
        return multa * 0.8  
    

tipo_de_infracao, multa, pontos = infracao(velocidade, vel_max)

multa = multado(reincidencia, tipo_de_infracao, multa)

multa = simular(multa, pagar_imediatamente)

curso = curso_reciclagem(tipo_de_infracao)

print("\n")
print(f"Placa: {placa}")
print(f"Motorista: {nome}")
print(f"Velocidade registrada: {velocidade} km/h")
print(f"Velocidade máxima permitida: {vel_max} km/h")
print(f"{tipo_de_infracao} - Multa de R$ {multa:.2f}, {pontos} pontos na CNH", end="")
if tipo_de_infracao == "Infração gravíssima":
    print(", suspensão da carteira.")

if reincidencia and tipo_de_infracao in ["Infração grave", "Infração gravíssima"]:
    print("Atenção: Multa dobrada por reincidência!")

if tipo_de_infracao == "Infração gravíssima":
    print("Atenção: CNH suspensa! Compareça ao Detran.")
    
if curso:
    print(f"Atenção: {curso}")
    
if pagar_imediatamente == "sim":
    print(f"Pagamento realizado! Você recebeu um desconto de 20%. Valor final: R$ {multa:.2f}")
else:
    print("Pagamento não realizado.")


