import matplotlib.pyptlot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]

titulo = "Gráfico de barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

#Legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Plotando gráfico de dispersão
plt.scatter(x, y, label="Meus pontos", color="k", marker=".", s=z)
plt.plot(x, y, color="#990000", linestyle="--")
plt.show()

#Salvando a imagem do gráfico na pasta atual
#Em PDF ele salva com uma maior qualidade, pois a imagem é vetorizada.
#plt.savefig("figura1.pdf")

#Caso não queira salvar em PDF e sim em png, para melhorar a qualidade da imagem configure o dpi.
plt.savefig("figura1.png", dpi=300)

"""
color: cor (ver exemplos abaixo)
label: rótulo
linestyle: estilo de linha (ver exemplos abaixo)
linewidth: largura da linha
marker: marcador (ver exemplos abaixo)

CORES (color)
'b' blue
'g' green
'r' red
'c' cyan
'm' magenta
'y' yellow
'k' black
'w' white

Marcadores (marker)
'.' point marker
',' pixel marker
'o' circle marker
'v' triangle_down marker
'^' triangle_up marker
'<' triangle_left marker
'>' triangle_right marker
'1' tri_down marker
'2' tri_up marker
'3' tri_left marker
'4' tri_right marker
's' square marker
'p' pentagon marker
'*' star marker
'h' hexagon1 marker
'H' hexagon2 marker
'+' plus marker
'x' x marker
'D' diamond marker
'd' thin_diamond marker
'|' vline marker
'_' hline marker

Tipos de linha (linestyle)
'-' solid line style
'--' dashed line style
'-.' dash-dot line style
':' dotted line style

Fonte: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
"""