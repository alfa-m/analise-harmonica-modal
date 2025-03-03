import pandas as pd
from procura_arquivos import procura

arquivos_v = procura("v_*.csv", "../arquivos_csv/")

#lista_de_nos = pd.read_csv("../arquivos_csv/lista_de_nos.csv", index_col=0)
lista_de_nos = pd.read_csv("../arquivos_csv/lista_de_nos.csv")
colunas = lista_de_nos.values

vetorVreal = []
vetorVimaginario = []

matrizVreal = pd.DataFrame(index=colunas, columns=colunas)
matrizVimaginario = pd.DataFrame(index=colunas, columns=colunas)

for arquivo in arquivos_v:
    arquivo_df = pd.read_csv("../arquivos_csv/{}".format(arquivo))
    matrizVreal = arquivo_df[arquivo_df.iloc[:,0] % 2 == 0]
    matrizVimaginario = arquivo_df[arquivo_df.iloc[:,0] % 2 == 1]
    matrizVreal = matrizVreal.iloc[:,1:]
    matrizVimaginario = matrizVimaginario.iloc[:,1:]
    matrizVreal.to_csv("../arquivos_csv/real_{}".format(arquivo))
    matrizVimaginario.to_csv("../arquivos_csv/imaginario_{}".format(arquivo))

print("Fim da criação dos arquivos com as matrizes V real e V imaginário")
