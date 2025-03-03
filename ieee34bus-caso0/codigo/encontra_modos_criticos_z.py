import pandas as pd
import numpy as np
from procura_arquivos import procura

matrizes_diagonais = procura("matriz_diagonal_z_real*.csv", "../arquivos_csv/")
lista_de_nos = pd.read_csv("../arquivos_csv/lista_de_nos.csv", index_col=0)
lista_de_nos = lista_de_nos.reset_index(drop=True)
lista_de_nos_numpy = lista_de_nos.to_numpy()
modos_criticos = pd.DataFrame(columns=["local","magnitude"])

for matriz in matrizes_diagonais:
    matriz_atual = pd.read_csv("../arquivos_csv/{}".format(matriz), index_col=0)
    matriz_atual.index = lista_de_nos
    matriz_atual.columns = lista_de_nos
    matriz_atual_complexa = matriz_atual.astype(complex)
    matriz_atual_real = matriz_atual_complexa.abs()
    matriz_atual_real.to_csv("../arquivos_csv/magnitude_{}".format(matriz))
    valores_maximos = matriz_atual_real.max()
    valores_maximos.to_csv("../arquivos_csv/valores_maximos_{}".format(matriz))
    valores_maximos_ordenados = valores_maximos.sort_values(ascending=False)
    valores_maximos_ordenados.to_csv("../arquivos_csv/valores_maximos_ordenados_{}".format(matriz))
    modo_critico = valores_maximos.max()
    indice_modo_critico = [i for i, x in enumerate(valores_maximos) if x == modo_critico]
    no_modo_critico = lista_de_nos_numpy[indice_modo_critico]
    modos_criticos.loc[matriz] = no_modo_critico, modo_critico

modos_criticos.to_csv('../arquivos_csv/modos_criticos_z.csv')
print("Modos críticos encontrados e salvos no arquivo 'modos_criticos_z.csv'")
