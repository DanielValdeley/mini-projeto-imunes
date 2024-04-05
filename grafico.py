import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Função para extrair a penúltima e última coluna de cada linha
def extrair_colunas(linha):
    colunas = linha.strip().split(',')
    if(len(colunas) < 14):
        print("len colunas < 14")
        return
    print(len(colunas))
    penultima_coluna = float(colunas[-2])
    ultima_coluna = float(colunas[-1])
    return penultima_coluna, ultima_coluna

bars1 = []
bars2 = []
# Abrir o arquivo e processar linha por linha
caminho_arquivo = "dados-cubic.csv"  # Substitua pelo caminho do seu arquivo
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

# # Create cyan bars
# plt.bar(r2, bars2, width = barWidth, color = 'cyan', edgecolor = 'black', capsize=7, label='taxa de transferência')
 
# # general layout
# plt.xticks([r + barWidth for r in range(len(bars1))])
# plt.ylabel('bps')
# plt.legend()
# plt.title(caminho_arquivo)
 
# # Show graphic
# plt.show()

def calcular_media_por_grupo(arquivo):
    # Dicionário para armazenar a soma e a contagem de cada grupo
    soma_por_grupo = {}
    contagem_por_grupo = {}

    # Abrir o arquivo
    with open(arquivo, 'r') as f:
        # Ler cada linha do arquivo
        for linha in f:
            # Dividir a linha em colunas
            colunas = linha.strip().split(',')

            # Extrair os valores das colunas 8 e 9
            valor_coluna8 = float(colunas[7])  # Assumindo que a indexação começa em 0
            valor_coluna9 = colunas[8]  # Assumindo que a indexação começa em 0

            # Atualizar a soma e a contagem para o grupo correspondente
            soma_por_grupo[valor_coluna9] = soma_por_grupo.get(valor_coluna9, 0) + valor_coluna8
            contagem_por_grupo[valor_coluna9] = contagem_por_grupo.get(valor_coluna9, 0) + 1

    # Calcular a média para cada grupo
    media_por_grupo = {}
    for grupo, soma in soma_por_grupo.items():
        contagem = contagem_por_grupo[grupo]
        media_por_grupo[grupo] = soma / contagem

    return media_por_grupo

print("bbbbbbbb")
print(calcular_media_por_grupo(caminho_arquivo))