#zip

lista1 = [1,2,3,4,5]
lista2 = ["abacata", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["R$2,00", "R$5,00", "Não tem preço", "Não tem preço", "Não tem preço"]

for numero, nome, preco in zip (lista1, lista2, lista3):
    print(numero,nome, preco)