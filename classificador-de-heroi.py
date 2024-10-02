def classificador_de_heroi():
    
    # Variável que recebe o input do usuário
    exp = int(input("Insira a experiência do heroi: "))

    # Estrutura condicional que define o output se baseando no valor do input
    if(exp < 1000):
        return "Ferro"
    elif(exp < 2000):
        return "Bronze"
    elif(exp < 5000): 
        return "Prata"
    elif(exp < 7000): 
        return "Ouro"
    elif(exp < 8000): 
        return "Platina"
    elif(exp < 9000): 
        return "Ascendente"
    elif(exp < 10000): 
        return "Imortal"
    else: 
        return "Radiante"
    
print(classificador_de_heroi())