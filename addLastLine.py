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
    # Carregar o arquivo CSV em um DataFrame do pandas
    df = pd.read_csv(arquivo, header=None)

    # Definir nomes das colunas
    df.columns = ['coluna1', 'coluna2', 'coluna3', 'coluna4', 'coluna5', 
                  'coluna6', 'coluna7', 'coluna8', 'coluna9', 'coluna10',
                  'coluna11', 'coluna12', 'coluna13', 'coluna14']

    # Converter a coluna 8 para tipo numérico
    df['coluna8'] = pd.to_numeric(df['coluna8'], errors='coerce')

    # Calcular a média da coluna 8 agrupada pela coluna 9
    media_por_grupo = df.groupby('coluna9')['coluna8'].mean()

    return media_por_grupo

