import sys
sys.setrecursionlimit(10**7)

class aresta:
    def __init__(self, x, y):
        self.x=x
        self.y=y

def adicionar_no(grafo, aresta):
    if aresta.x not in grafo:
        grafo[aresta.x] = []
    if aresta.y not in grafo:
        grafo[aresta.y] = []
    grafo[aresta.x].append(aresta.y)

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

    return len(componentes)

# Execução principal
##################################################

dados = list(map(int, sys.stdin.read().split()))

if not dados:
    sys.exit()

n = dados[0]
idx = 1

grafo = {}    

for i in range(n):
    x = dados[idx]
    y = dados[idx + 1]
    idx += 2

    ar = aresta(x, y)
    adicionar_no(grafo, ar)

for i in range(1, n+1):
    if i not in grafo:
        grafo[i] = []

componentes = kosaraju(grafo)

if componentes == 1:
    print('S')
else:
    print('N')
