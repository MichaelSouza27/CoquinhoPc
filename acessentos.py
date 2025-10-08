fileira_1 = [1, 2, 3, 4, 5, 6, 7, 8] 
fileira_2 = [1, 2, 3, 4, 5, 6, 7, 8]
fileira_3 = [1, 2, 3, 4, 5, 6, 7, 8]
fileira_4 = [1, 2, 3, 4, 5, 6, 7, 8]
fileira_5 = [1, 2, 3, 4, 5, 6, 7, 8]


print("Fileira 1:", fileira_1)
print("Fileira 2:", fileira_2)
print("Fileira 3:", fileira_3)
print("Fileira 4:", fileira_4)
print("Fileira 5:", fileira_5)

print()

e = input("Se deseja reservar um assento digite (s): ")

while e == "s":
    fileira = int(input("Digite a fileira (1-5): "))
    assento = int(input("Digite o assento (1-8): "))
    print()
    if e == "n":
        print("Obrigado por usar nosso sistema de reservas!")
        
    if fileira == 1:
        print("Fileira 1 reservada.")
        fileira_1[assento - 1] = "X"
        print("Fileira 1:", fileira_1)
        print()
        
        print("Deseja reservar outro assento? (s/n) ou você quer cancelar a reserva? (c)")
        print()
        e = input()
        if e == "n":
            print("Obrigado por usar nosso sistema de reservas!")
            break
        elif e == "s":
            continue
        elif e == "c":
         print("Acessento cancelado")
        
    
    elif fileira == 2:
        print("Fileira 2 reservada.")
        fileira_2[assento - 1] = "X"
        print("Fileira 2:", fileira_2)
        
        print("Deseja reservar outro assento? (s/n)")
        e = input()
        if e == "n":
            print("Obrigado por usar nosso sistema de reservas!")
            break
        elif e == "s":
            continue
        elif e == "c":
         print("Acessento cancelado")
           
    
    elif fileira == 3:
        print("Fileira 3 reservada.")
        fileira_3[assento - 1] = "X"
        print("Fileira 3:", fileira_3)
    
        
        print("Deseja reservar outro assento? (s/n)")
        e = input()
        if e == "n":
            print("Obrigado por usar nosso sistema de reservas!")
            break
        elif e == "s":
            continue
        elif e == "c":
            print("Acessento cancelado")
            
        
    
    
    elif fileira == 4:
        print("Fileira 4 reservada.")
        fileira_4[assento - 1] = "X"
        print("Fileira 4:", fileira_4)
        
        print("Deseja reservar outro assento? (s/n)")
        e = input()
        if e == "n":
            print("Obrigado por usar nosso sistema de reservas!")
            break
        elif e == "s":
            continue
        elif e == "c":
             print("Acessento cancelado")
          
    
    elif fileira == 5:
        print("Fileira 5 reservada.")
        fileira_5[assento - 1] = "X"
        print("Fileira 5:", fileira_5)
        
        print("Deseja reservar outro assento? (s/n)")
        e = input()
        if e == "n":
            print("Obrigado por usar nosso sistema de reservas!")
            break
        elif e == "s":
            continue
        elif e == "c":
             print("Acessento cancelado")
        
    
    
    else:
        print("Fileira inválida.")
        

 
    