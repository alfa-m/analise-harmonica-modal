import py_dss_interface
import pandas as pd
import numpy as np
import os
import pathlib

# Inicializa o objeto DSS
dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")

# Adiciona o path e compila o arquivo .dss
script_path = os.path.dirname(os.path.abspath(__file__))
dss_file = pathlib.Path(script_path).joinpath("ieee34Mod1.dss")
dss.text("Compile [{}]".format(dss_file))

# Adiciona dados de coordenadas das barras
dss.text("Buscoords BusCoords.dat")

# Cria variaveis contendo o nome das linhas, barras e nós
nomesLinhas = dss.lines.names
nomesBarras = dss.circuit.buses_names
nomesNos = dss.circuit.nodes_names

# Realiza a solução do fluxo de potência para obter os valores de magnitude e fase das tensões e correntes

dss.solution.solve()

# Remove demais fontes harmonicas
dss.text("Spectrum.DefaultLoad.NumHarm=1")

# Define o espectro de frequências a serem analisadas
harmonicos = np.arange(1,50.001,(0.5/60)).tolist()
dss.text("New spectrum.espectroharmonico numharm={} csvfile=espectro_harmonico.csv".format(str(len(harmonicos))))

#  Adiciona a fonte de corrente harmônica de sequência positiva
node = nomesNos[23]
barra_e_no = node.rsplit(".")
barra = barra_e_no[0]
no = barra_e_no[1]
dss.text("New Isource.scansource bus1={} amps=1 spectrum=espectroharmonico".format(node))

# Adiciona um monitor em cada linha
for i in range(len(nomesLinhas)):
    linha = nomesLinhas[i]
    dss.text("New Monitor.{} Line.{} 1 mode=0".format((linha+"_"+barra+"_"+no), linha))

# Salva nomes dos monitores
nomesMonitores = dss.monitors.names

dss.solution.solve()

# Seleciona o modo de solução harmonic
dss.text("Set mode=harmonic")
dss.solution.solve()

# Plota todos os monitores
for k in range(len(nomesMonitores)):
   monitor = nomesMonitores[k]
   dss.text("Plot monitor object={} channels=(1 3 5)".format(monitor))

# Exporta todos os valores dos monitores
dss.text("Export monitors all")

print("Análise harmônica no nó {} finalizada".format(node))
