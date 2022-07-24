import math
import pandas as pd


class PdmBRKGA:

    def __init__(self, num_vet=0, num_edg=0, mat_adj=None, list_adj: list = None):
        self.num_vet = num_vet
        self.num_edg = num_edg

    def addEdge(self, u, v, result):
        if u < self.num_vet and v < self.num_vet:
            self.mat_adj[u][v] = result
            self.lista_adj[u].append(result)
        else:
            print("Aresta Invalida")

    def readFile(self, nameFile):

        try:
            fileCSV = pd.read_csv(nameFile, sep=';', encoding='utf-8')

            return fileCSV
        except:
            print("Erro ao ler arquivo CSV.")

    def firstStep(self, fileCSV):

        self.num_vet = len(fileCSV)
        self.mat_adj = [[0 for _ in range(self.num_vet)]
                        for _ in range(self.num_vet)]
        self.lista_adj = [[] for i in range(self.num_vet)]

        for i in range(len(fileCSV)):
            for j in range(len(fileCSV)):

                if i == j:
                    result = 0.0
                    self.addEdge(i, j, result)

                elif self.mat_adj[i][j] == 0:
                    result = math.sqrt((
                        (float(fileCSV['valence'][i]) - (float(fileCSV['valence'][j])))**2)
                        + ((float(fileCSV['acousticness'][i]) -
                            (float(fileCSV['acousticness'][j])))**2)
                        + ((float(fileCSV['danceability'][i]) -
                            (float(fileCSV['danceability'][j])))**2)
                        + ((float(fileCSV['energy'][i]) -
                            (float(fileCSV['energy'][j])))**2)
                        + ((float(fileCSV['instrumentalness'][i]) -
                            (float(fileCSV['instrumentalness'][j])))**2)
                        + ((float(fileCSV['liveness'][i]) -
                            (float(fileCSV['liveness'][j])))**2)
                        + ((float(fileCSV['speechiness'][i]) -
                            (float(fileCSV['speechiness'][j])))**2))

                    self.addEdge(i, j, result)
                    self.addEdge(j, i, result)

    def run(self, nameFIle):
        self.firstStep(self.readFile(nameFIle))
