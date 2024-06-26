import subprocess
import csv

##### inicializacao de dados
alg = ['cubic', 'reno']
BER = ['100000', '1000000']
e2e_delay = ['10000', '100000'] #10ms, 100ms
trafego_bg = ['500', '900']
repeticao = 8


# trafego TCP
def client_pc1(proto):
    print("[START]: client_pc1")
    return "sudo himage pc1@i3cf1 iperf -c 10.0.2.20 -y C -Z " + proto + " >> dados-" + proto + ".csv"

# trafego bg UDP
def client_pc3(bg):
    print("[START]: client_pc3")
    return "sudo himage pc3@i3cf1 iperf -c 10.0.4.20 -u -b " + bg

# trafego bg UDP
def client_pc4(bg):
    print("[START]: client_pc4")
    return "sudo himage pc4@i3cf1 iperf -c 10.0.3.20 -u -b " + bg

def add_coluna(linha, nova_coluna):
        linha.append(nova_coluna)
        return linha

def cabecalho(arquivo_entrada):
        f = open(arquivo_entrada, "a")
        f.write("1,2,3,4,5,6,7,8,9,10,11,12,13,14\n")
        f.close()

def add_coluna_ultima_linha(arquivo_entrada, arquivo_saida, nova_coluna):
    linhas_arquivo = []

    with open(arquivo_entrada, 'r', newline='') as arquivo_entrada:
        leitor_csv = csv.reader(arquivo_entrada)
        for linha in leitor_csv:
            linhas_arquivo.append(linha)

    linhas_arquivo[-1] = add_coluna(linhas_arquivo[-1], nova_coluna)

    with open(arquivo_saida, 'w', newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida)
        for linha in linhas_arquivo:
            escritor_csv.writerow(linha)

cabecalho("dados-cubic.csv")
cabecalho("dados-reno.csv")
for rep in range(repeticao):
    print("[REP]: ", rep)
    for proto in alg:
        print("[PROTO]: ", proto)
        for ber in BER:
            print("[BER]: ", ber)
            for bg in trafego_bg:
                print("[BG]: ", bg)
                for e2e in e2e_delay:
                    print("[DELAY]: ", e2e)
                    
                    subprocess.run("sudo vlink -BER " + "0" + " pc1:router1@i3cf1", shell=True)
                    subprocess.run("sudo vlink -BER " + ber + " -d " + e2e + " router1:router2@i3cf1", shell=True)
                    subprocess.run("sudo vlink -BER " + "0" + " router2:pc2@i3cf1", shell=True)

                    subprocess.run("sudo vlink -BER " + "0" + " pc2:router2@i3cf1", shell=True)
                    subprocess.run("sudo vlink -BER " + ber + " -d " + e2e + " router2:router1@i3cf1", shell=True)
                    subprocess.run("sudo vlink -BER " + "0" + " router1:pc1@i3cf1", shell=True)

                    subprocess.run("sudo vlink -BER " + "0" + " pc3:router1@i3cf1", shell=True)
                    subprocess.run("sudo vlink -BER " + ber + " -d " + e2e + " router1:router2@i3cf1", shell=True)
                    subprocess.run("sudo vlink -BER " + "0" + " router2:pc4@i3cf1", shell=True)

                    subprocess.run("sudo vlink -BER " + "0" + " pc4:router2@i3cf1", shell=True)
                    subprocess.run("sudo vlink -BER " + ber + " -d " + e2e + " router2:router1@i3cf1", shell=True)
                    subprocess.run("sudo vlink -BER " + "0" + " router1:pc3@i3cf1", shell=True)

                    # TCP - reno e cubic
                    subprocess.run(client_pc1(proto), shell=True)
                    add_coluna_ultima_linha("dados-" + proto + ".csv","dados-" + proto + ".csv", int(rep))
                    add_coluna_ultima_linha("dados-" + proto + ".csv","dados-" + proto + ".csv", proto)
                    add_coluna_ultima_linha("dados-" + proto + ".csv","dados-" + proto + ".csv", int(ber))
                    add_coluna_ultima_linha("dados-" + proto + ".csv","dados-" + proto + ".csv", int(bg))
                    add_coluna_ultima_linha("dados-" + proto + ".csv","dados-" + proto + ".csv", int(e2e))
                    
 
                    # UDP - trafego de background
                    subprocess.run(client_pc3(bg), shell=True)
                    subprocess.run(client_pc4(bg), shell=True)
