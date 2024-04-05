import numpy as np
import matplotlib.pyplot as plt

# Função para extrair a penúltima e última coluna de cada linha
def extrair_colunas(linha):
    colunas = linha.strip().split(',')
    penultima_coluna = float(colunas[-2])
    ultima_coluna = float(colunas[-1])
    return penultima_coluna, ultima_coluna

bars1 = []
bars2 = []
# Abrir o arquivo e processar linha por linha
caminho_arquivo = "dados-reno.csv"  # Substitua pelo caminho do seu arquivo
with open(caminho_arquivo, 'r') as arquivo:
    for linha in arquivo:
        penultima, ultima = extrair_colunas(linha)
        # print("Penúltima coluna:", penultima)
        # print("Última coluna:", ultima)
        bars1.append(penultima)
        bars2.append(ultima) 


print("Penúltima coluna:", bars1)
print("última coluna:", bars2)

# width of the bars
barWidth = 0.3

# The x position of bars
r1 = np.arange(len(bars1))
r2 = [x + barWidth for x in r1]

print(r1)
print("asdasd")
print(r2)
 
# Create blue bars
# plt.bar(r1, bars1, width = barWidth, color = 'blue', edgecolor = 'black', capsize=7, label='largura de banda')

# Create cyan bars
plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', capsize=7, label='taxa de transferência')
 
# general layout
plt.xticks([r + barWidth for r in range(len(bars1))])
plt.ylabel('bps')
plt.legend()
plt.title(caminho_arquivo)
 
# Show graphic
plt.show()
