import heapq

class Aresta:
    def __init__(self, x, y, w):
        self.x=x
        self.y=y
        self.w=w

def adicionar_no(grafo, aresta):
    if aresta.x not in grafo:
        grafo[aresta.x] = {}
    if aresta.y not in grafo:
        grafo[aresta.y] = {}

    grafo[aresta.x][aresta.y] = aresta.w
    grafo[aresta.y][aresta.x] = aresta.w
        
        
def prim(grafo, inicio, inverter=False):
    visitados = set()
    heap = []
    custo_total = 0

    visitados.add(inicio)

    for vizinho, peso in grafo[inicio].items():
        peso_heap = -peso if inverter else peso
        heapq.heappush(heap, (peso_heap, inicio, vizinho))

    while heap and len(visitados) < len(grafo):
        peso, u, v = heapq.heappop(heap)

        if v in visitados:
            continue

        visitados.add(v)
        custo_total += peso

        for vizinho, novo_peso in grafo[v].items():
            if vizinho not in visitados:
                peso_heap = -novo_peso if inverter else novo_peso
                heapq.heappush(heap, (peso_heap, v, vizinho))

    return custo_total

################################################################

n = int(input())

grafo = {}

for i in range(n):
    u, v, w = map(int, input().split())
    aresta = Aresta(u, v, w)
    adicionar_no(grafo, aresta)

inicio = next(iter(grafo))

menor_custo = prim(grafo, inicio)
maior_custo = prim(grafo, inicio, True) * -1


print(maior_custo)
print(menor_custo)



