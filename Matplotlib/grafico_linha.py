import matplotlib.pyptlot as plt

x = [1, 2, 5]
y = [2, 3, 7]

#Título do gráfico
plt.title("Meu primeiro gráfico com Python")

#Eixos
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

#Plotando gráfico de linhas
plt.plot(x, y)
plt.show()