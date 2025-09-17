def comparar_cdb_poupanca(valor, dias):
    cdi_ano = 0.06  
    cdb_taxa = 1.10  
    selic_ano = 0.085 
    poupanca_juros_mes_alta = 0.005 
    poupanca_juros_mes_baixa = 0.007* selic_ano  
    
    tempo_anos = dias / 365
    rendimento_cdb = valor * (1 + cdi_ano * cdb_taxa) * tempo_anos

    if dias < 30:
        print("A poupança não terá rendimento, pois exige aniversário mensal")
        rendimento_poupanca = valor 
    else:
        if selic_ano > 0.085:
            rendimento_poupanca = valor * (1 + poupanca_juros_mes_alta) * (tempo_anos * 12)
        else:
            rendimento_poupanca = valor * (1 + poupanca_juros_mes_baixa) * (tempo_anos * 12)
    
    print(f"Valor investido: R$ {valor:.2f}")
    print(f"Rendimento CDB: R$ {rendimento_cdb:.2f}")
    print(f"Rendimento Poupança: R$ {rendimento_poupanca:.2f}")
    
    if rendimento_cdb > rendimento_poupanca:
        print("O CDB foi mais vantajoso")
    elif rendimento_poupanca > rendimento_cdb:
        print("A Poupança foi mais vantajosa")
    else:
        print("Ambos os investimentos tiveram o mesmo rendimento") 
    
comparar_cdb_poupanca(1000, 365)