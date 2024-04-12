import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

repeticao = 9   #coluna
algoritimo = 10
taxa = 8
ber = 11
bg = 12
delay = 13

df = pd.read_csv("dados-reno.csv", encoding='utf-8-sig', sep='\s*,\s*', engine='python')
# media_reno_bg_500_900 = df.groupby([df.columns[bg]])[[df.columns[taxa]]].mean().reset_index()
# media_reno_bg_500_900.to_csv("media_reno_bg_500_900.csv")
# print("media_reno_bg_500_900: ", media_reno_bg_500_900)

# media_reno_ber_100000_1000000 = df.groupby([df.columns[ber]])[[df.columns[taxa]]].mean().reset_index()
# media_reno_ber_100000_1000000.to_csv("media_reno_ber_100000_1000000.csv")


media_reno_delay_10000_100000 = df.groupby([df.columns[delay]])[[df.columns[taxa]]].mean().reset_index()
media_reno_delay_10000_100000.to_csv("media_reno_delay_10000_100000.csv")


# Função para extrair a penúltima e última coluna de cada linha
def extrair_colunas(linha):
    colunas = linha.strip().split(',')
    print(len(colunas))
    coluna_taxa = float(colunas[2])
    return coluna_taxa

bars1 = []

# Abrir o arquivo e processar linha por linha
caminho_arquivo = "media_reno_delay_10000_100000.csv"  # Substitua pelo caminho do seu arquivo
with open(caminho_arquivo, 'r') as arquivo:
    count = 0               # contador para nao capturar a primeira linha (cabecalho)
    for linha in arquivo:
        if(count > 0):
            coluna_taxa = extrair_colunas(linha)
            bars1.append(coluna_taxa)
        count += 1

print("Penúltima coluna:", bars1)

# width of the bars
barWidth = 1

# The x position of bars
# r1 = np.arange(len(bars1))
r1 = np.array([0,1])

print("r1: ", r1)
print("bars1: ", bars1)
 
# Create blue bars
plt.bar(r1, bars1, color='green')
# general layout
plt.xticks([r for r in range(len(bars1))],[10000,100000])

plt.ylabel('bps')
plt.legend()
plt.title(caminho_arquivo)

# Show graphic
plt.show()
