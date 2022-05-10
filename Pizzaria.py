print("OLÁ, SEJA BEM-VINDO A PIZZARIA DO ERICK")
nome = (input("Digite o seu nome:"))
Tel = (input("Digite o seu telefone:"))  
cep = (input("Digite o seu CEP:"))
endereço = (input("Digite o seu endereço:"))
acrescentar = "s"
finalizar = "n"
TOTAL = 0
precospizza=[0,27.9,30.99,40.9,29.9,35.9,38.9,25.9,30.99,39.9,0]
while acrescentar == "s":
    cardapio = """
    NOSSOS SABORES\n
    1 Portuguesa - R$ 27,90\n 
    2 4 Queijos - R$ 30,99\n 
    3 Califórnia- R$ 40,90\n 
    4 Beijinho - R$ 29,99\n 
    5 Baiana - R$ 35,90\n 
    6 Atum - R$ 38,99\n 
    7 Dois Amores - R$ 25,90\n 
    9 Nutella- R$ 39,90\n
    10 Personalizada - R$ 0,00\n"""
    print(cardapio)
    indice = int(input("Digite o número da pizza:\n"))
    TOTAL = TOTAL + precospizza[indice]
    print(f"O subtotal do pedido é:{TOTAL:,.2f}")
    acrescentar=input("Deseja acrescentar mais alguma pizza no pedido?")
    if finalizar == "n":
        print("Estamos enviando !")




    
    




