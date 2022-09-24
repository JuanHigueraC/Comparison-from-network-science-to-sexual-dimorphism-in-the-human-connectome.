# -*- coding: utf-8 -*-
"""Proyecto biofísica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g0rTtwiYbLlo4W5I16rK5ObomwgUrzVK
"""

#importamos librerias, networkx para grafos, matplotlib para plotear, pandas para trabajar los datos y numpy par ala matriz de adyacencia
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Commented out IPython magic to ensure Python compatibility.
#este codigo nos permite importar el drive a google colab, esto con el fin de cargar los archivos
from google.colab import drive
drive.mount('/gdrive')
# %cd /gdrive

#se ubica la carpeta con los archivos en el drive
cd "/gdrive/MyDrive/Física Juan Higuera/Materias Pregrado/9no/Biofísica avanzada/Proyecto Biofísica/Conectomas Biofísica 2"

#se cargan los conectomas de mujeres para distintos consensos
Female_1 = nx.read_graphml("Female 1.graphml")
Female_10 = nx.read_graphml("Female 10.graphml")
Female_20 = nx.read_graphml("Female 20.graphml")
Female_30 = nx.read_graphml("Female 30.graphml")
Female_40 = nx.read_graphml("Female 40.graphml")
Female_50 = nx.read_graphml("Female 50.graphml")
Female_60 = nx.read_graphml("Female 60.graphml")
Female_70 = nx.read_graphml("Female 70.graphml")
Female_80 = nx.read_graphml("Female 80.graphml")
Female_90 = nx.read_graphml("Female 90.graphml")
Female_100 = nx.read_graphml("Female 100.graphml")

#se cargan los conectomas de hombres para distintos consensos
Male_1 = nx.read_graphml("Male 1.graphml")
Male_10 = nx.read_graphml("Male 10.graphml")
Male_20 = nx.read_graphml("Male 20.graphml")
Male_30 = nx.read_graphml("Male 30.graphml")
Male_40 = nx.read_graphml("Male 40.graphml")
Male_50 = nx.read_graphml("Male 50.graphml")
Male_60 = nx.read_graphml("Male 60.graphml")
Male_70 = nx.read_graphml("Male 70.graphml")
Male_80 = nx.read_graphml("Male 80.graphml")
Male_90 = nx.read_graphml("Male 90.graphml")
Male_100 = nx.read_graphml("Male 100.graphml")

#encapsulamos los conectomas en listas para facilitar el calculo de medidas
Males = [Male_1,Male_10,Male_20,Male_30,Male_40,Male_50,Male_60,Male_70,Male_80,Male_90,Male_100]
Females = [Female_1,Female_10,Female_20,Female_30,Female_40,Female_50,Female_60,Female_70,Female_80,Female_90,Female_100]

#Está función remueve los nodos isolados de un grafo
def remove_isolates(Grafo):
  isolados = list(nx.isolates(Grafo))
  Grafo.remove_nodes_from(isolados)
  return Grafo

#se remueven los isolados para todos los conectomas
for grafo in Males:
  remove_isolates(grafo) 
for grafo in Females:
  remove_isolates(grafo)

#Se extrae la matriz de adyacencia y se gráfica
Adj = nx.to_numpy_matrix(Male_1)
fig = plt.figure(figsize=(15,8))
plt.imshow(Adj,vmax= 1, vmin = 0)
plt.title("Plot 2D array")
plt.show()

#se calculan e imprimen los 10 nodos mas centrales segun el grado
degreefem = nx.degree_centrality(Female_20)
degreefem_ord = sorted(degreefem.items(), key =lambda x: x[1],reverse = True)

degreemal = nx.degree_centrality(Male_20)
degreemal_ord = sorted(degreemal.items(), key =lambda x: x[1],reverse = True)

for i in range(10):
  print(degreemal_ord[i],degreefem_ord[i])

#se calculan e imprimen los 10 nodos mas centrales segun eigenvector
degreefem = nx.eigenvector_centrality(Female_20)
degreefem_ord = sorted(degreefem.items(), key =lambda x: x[1],reverse = True)

degreemal = nx.eigenvector_centrality(Male_20)
degreemal_ord = sorted(degreemal.items(), key =lambda x: x[1],reverse = True)

for i in range(10):
  print(degreemal_ord[i],degreefem_ord[i])

#se construye el grafo de maxima entropia

degree_secuence = []
#primero extraemos el grado de la red real
deg = nx.degree(Male_20)
for i in deg:
  degree_secuence.append(i[1])
#construimos el grafo con los grados requeridos
Gmaxent = nx.havel_hakimi_graph(degree_secuence)
#aleatorizamos el grafo
Gmaxent = nx.double_edge_swap(Gmaxent, nswap = 10000,max_tries = 10000000000)

#se miden los grados para el consenso del 20% y se plotean
medida201 =nx.degree_centrality(Males[2])
medida202 = nx.degree_centrality(Females[2])

medida = medida201
medida_ord = sorted(medida.items(), key =lambda x: x[1],reverse = True) #está linea es para ordenar el diccionario acorde al valor
Measuremales = []
for i in range(len(medida_ord)):
  Measuremales.append(medida_ord[i][1])
plt.plot(Measuremales,color = "red", label = 'Males')

medida = medida202
medida_ord = sorted(medida.items(), key =lambda x: x[1],reverse = True) #está linea es para ordenar el diccionario acorde al valor
Measurefemales = []
for i in range(len(medida_ord)):
  Measurefemales.append(medida_ord[i][1])
plt.plot(Measurefemales,color = "green", label = 'Females')

plt.legend(loc=1)
plt.xlabel("Nodos")
plt.ylabel("Degree Centrality")
plt.title("Degree Centrality al consenso del 20%")
plt.savefig("Eigenal20.jpg", bbox_inches='tight', dpi=300)

#se calcula eigenvector para los grafos de hombre, mujer y maxima entropia
medida201 = nx.eigenvector_centrality(Males[2], max_iter = 1000)
medida202 = nx.eigenvector_centrality(Females[2], max_iter = 1000)
medida203 = nx.eigenvector_centrality(Gmaxent,max_iter = 10000)

#el codigo para plotear cada medida es igual a los otros

Betwn = medida203
#se ordena la medida
Betwn_ord = sorted(Betwn.items(), key =lambda x: x[1],reverse = True) 
Measure = []
#se mingresan los valores en una lista y plotean
for i in range(len(Betwn_ord)):
  Measure.append(Betwn_ord[i][1])
plt.plot(Measure,color = "blue", label = 'Maxent')

Betwn = medida201
Betwn_ord = sorted(Betwn.items(), key =lambda x: x[1],reverse = True) 
Measure = []
for i in range(len(Betwn_ord)):
  Measure.append(Betwn_ord[i][1])
plt.plot(Measure,color = "red", label = 'Males')

Betwn = medida202
#esta linea es para ordenar el diccionario acorde al valor
Betwn_ord = sorted(Betwn.items(), key =lambda x: x[1],reverse = True)
Measure = []
for i in range(len(Betwn_ord)):
  Measure.append(Betwn_ord[i][1])
plt.plot(Measure,color = "green", label = 'Females')

plt.legend(loc=1)
plt.xlabel("Nodos")
plt.ylabel("Eigenvector centrality")
plt.title("Eigenvector centrality al consenso del 20%")
plt.savefig("Eigenal20.jpg", bbox_inches='tight', dpi=300)

#el siguiende codigo es para plotear el numero de nodos para cada consenso
edges_males = []
edges_females = []

for i in Males:
  edges_males.append(nx.number_of_nodes(i))
for i in Females:
  edges_females.append(nx.number_of_nodes(i))
plt.figure(figsize=(15,8))
plt.plot(edges_males)
plt.plot(edges_females)

#el siguiente codigo es para plotear el numero de enlaces para cada consenso
edges_males = []
edges_females = []

for i in Males:
  edges_males.append(nx.global_efficiency(i))
for i in Females:
  edges_females.append(nx.global_efficiency(i))
plt.figure(figsize=(15,8))
plt.plot(edges_males)
plt.plot(edges_females)