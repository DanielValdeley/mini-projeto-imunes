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
