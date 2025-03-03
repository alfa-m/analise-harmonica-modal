import pandas as pd
from procura_arquivos import procura

lista_de_harmonicos = pd.read_csv("../arquivos_csv/espectro_harmonico.csv").iloc[:,1]
lista_de_nos = pd.read_csv("../arquivos_csv/lista_de_nos.csv", index_col=0)["0"]
arquivos_v_real = procura("real_v_node*.csv", "../arquivos_csv/")

indice = 0
for harmonico in lista_de_harmonicos:
    print("Harmônico atual: ", harmonico)
    harmonico_df = pd.DataFrame()
    for i in range(len(lista_de_nos)):
        node = lista_de_nos.iloc[i]
        print("Nó atual: ", node)

        for arquivo in arquivos_v_real:
            nome_arquivo_dividido = arquivo.rsplit("_")
            final_nome_arquivo = nome_arquivo_dividido[-1]
            final_nome_arquivo_sem_extensao = final_nome_arquivo.rsplit(".csv")[0]

            if final_nome_arquivo_sem_extensao == node:
                caminho = "../arquivos_csv/{}".format(arquivo)
                arquivo_df = pd.read_csv(caminho, index_col=0)
                harmonico_df[node] = arquivo_df.iloc[:,indice]
                break
            else:
                continue

    harmonico_df.index = lista_de_nos
    harmonico_df.to_csv("../arquivos_csv/z_real_harmonico_{}.csv".format(harmonico))
    indice = indice + 1

print("Matrizes Z real criadas")
