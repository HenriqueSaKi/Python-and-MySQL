#Enumerate

lista = ["abacate", "bola", "cachorro"]

#Beginner way
for i in range(len(lista)):
    print(i, lista[i]) 

print ("-----------------------------")

#Advanced way
for i, nome in enumerate(lista):
    print (i, nome)