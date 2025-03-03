import pandas as pd
import numpy as np
from procura_arquivos import procura

lista_de_matrizes_z = procura('Z_real_harmonico*.csv', '../arquivos_csv/')

for matriz_z in lista_de_matrizes_z:
    caminho = "../arquivos_csv/{}".format(matriz_z)
    matriz_z_df = pd.read_csv(caminho, index_col=0)
    autovalores_matriz_z, autovetores_matriz_z = np.linalg.eig(matriz_z_df)
    matriz_z_diagonal = np.diag(autovalores_matriz_z)
    matriz_z_diagonal_df = pd.DataFrame(matriz_z_diagonal)
    matriz_z_diagonal_df.to_csv("../arquivos_csv/matriz_diagonal_{}".format(matriz_z))
    autovetores_matriz_z_df = pd.DataFrame(autovetores_matriz_z)
    autovetores_matriz_z_df.to_csv("../arquivos_csv/autovetores_{}".format(matriz_z))

print("Matrizes Z real decompostas diagonalmente e matrizes de autovetores obtidas")
