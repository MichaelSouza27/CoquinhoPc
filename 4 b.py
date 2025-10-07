
cafe = 20
escova = 10
oleo = 15
congelados = 30
sal = 5

c = (input("Escreva comprar: "))

if c == "comprar":
    
    print()
    print("Esse é o estoque atual:")
    
    cafe = cafe - 4
    print("Café no estoque:", cafe)
    
    congelados = congelados - 2
    print("Congelados no estoque:", congelados)
    
    sal = sal + 10
    print("Sal no estoque:", sal)
    
    oleo = 15
    print("Óleo no estoque:", oleo)
    
else:
    print("Comando inválido, tente novamente.")

