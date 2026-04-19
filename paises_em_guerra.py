import sys

###################################################################################

class aresta:
    def __init__(self, x, y, h):
        self.x=x
        self.y=y
        self.h=h

###################################################################################

def kosaraju(grafo):
    visitado = set()
    ordem = []

    def dfs1(u):
        visitado.add(u)
        for v in grafo[u]:
            if v not in visitado:
                dfs1(v)
        ordem.append(u)

    for u in grafo:
        if u not in visitado:
            dfs1(u)

    gt = {u: [] for u in grafo}
    for u in grafo:
        for v in grafo[u]:
            gt[v].append(u)

    visitado.clear()
    componentes = []

    def dfs2(u, comp):
        visitado.add(u)
        comp.append(u)
        for v in gt[u]:
            if v not in visitado:
                dfs2(v, comp)

    for u in reversed(ordem):
        if u not in visitado:
            comp = []
            dfs2(u, comp)
            componentes.append(comp)

    return componentes

###################################################################################

def calcular_dijkstra(grafo, origem, destino, id_scc):

  # Inicialização das distâncias com infinito, exceto a origem que é zero
    distancias = {v: sys.maxsize for v in grafo}
    distancias[origem] = 0

    # Conjunto de vértices visitados
    visitados = set()

    while visitados != set(distancias):
        # Encontra o vértice não visitado com menor distância atual
        vertice_atual = None
        menor_distancia = sys.maxsize
        for v in grafo:
            if v not in visitados and distancias[v] < menor_distancia:
                vertice_atual = v
                menor_distancia = distancias[v]
        
        if vertice_atual is None:
            break

        # Marca o vértice atual como visitado
        visitados.add(vertice_atual)

        # Atualiza as distâncias dos vértices vizinhos
        for vizinho, peso in grafo[vertice_atual].items():
            if id_scc[vertice_atual] == id_scc[vizinho]:
                peso = 0
            if distancias[vertice_atual] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[vertice_atual] + peso

  # Retorna as distâncias mais curtas a partir da origem

    if distancias[destino] == sys.maxsize:
        return None

    return distancias[destino]

###################################################################################

def adicionar_no(grafo, aresta):
    # grafo[aresta.x] = {aresta.y : aresta.h}
    if aresta.x not in grafo:
        grafo[aresta.x] = {}
    grafo[aresta.x][aresta.y] = aresta.h

###################################################################################

while True:
    # Recebe quantidade de vértices e de arestas
    n, e = map(int, input().split())

    # Encerra o laço
    if n == 0 and e == 0:
        break

    grafo = {}    

    # Receber arestas
    for i in range(e):
        x, y, h = map(int, input().split())
        ar = aresta(x, y, h)
        adicionar_no(grafo, ar)
    
    for i in range(1, n+1):
        if i not in grafo:
            grafo[i] = {}
    
    # Criar as componentes
    componentes = kosaraju(grafo)
    id_scc = {}
    for i, css in enumerate(componentes):
        for v in css:
            id_scc[v] = i

    # Inteiro K consultas
    k = int(input())

    distancias_das_consultas = []

    for i in range(k):
        
        o, d = map(int, input().split()) #Consulta

        distancia = calcular_dijkstra(grafo, o, d, id_scc) # Calcula a distancia da consulta de o pra d
        distancias_das_consultas.append(distancia)

    for d in distancias_das_consultas:
        if d is None:
            print("Nao e possivel entregar a carta")
        else:
            print(d)
    print()

###################################################################################

