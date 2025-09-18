a,b = 0,1
sequencia = []

n = int(input("Escolha um numero: "))

while len (sequencia) < n:
    sequencia.append(a)
    a,b = b , a + b

print(sequencia)


    
 