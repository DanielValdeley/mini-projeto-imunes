def adicionar_coluna_ultima_linha(arquivo_entrada, arquivo_saida, nova_coluna):
    # Função para adicionar uma nova coluna ao final de uma linha
    def adicionar_coluna(linha, nova_coluna):
        linha.append(nova_coluna)
        return linha

    # Lista para armazenar as linhas do arquivo
    linhas_arquivo = []

    # Lendo o arquivo e armazenando as linhas
    with open(arquivo_entrada, 'r', newline='') as arquivo_entrada:
        leitor_csv = csv.reader(arquivo_entrada)
        for linha in leitor_csv:
            linhas_arquivo.append(linha)

    # Adicionando a nova coluna apenas à última linha
    linhas_arquivo[-1] = adicionar_coluna(linhas_arquivo[-1], nova_coluna)

    # Escrevendo todas as linhas, incluindo a última modificada, no arquivo de saída
    with open(arquivo_saida, 'w', newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida)
        for linha in linhas_arquivo:
            escritor_csv.writerow(linha)





###################
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

