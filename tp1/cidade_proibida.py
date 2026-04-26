from collections import deque

class Vertice:
    def __init__(self, valor):
        self.valor=valor
        self.d = 0

def criar_grafo(g, x, y):
    if x not in g:
        g[x] = []
    if y not in g:
        g[y] = []
    g[x].append(y)
    g[y].append(x)

def bfs(grafo, c, r, e):
    visitados = []
    fila = deque([c])
    visitados.append(c) 
    while fila:
        u = fila.popleft()
        if u.valor == e:
            continue

        for v in grafo[u]:
            if v.valor == e:
                continue
            if v not in visitados:
                visitados.append(v)
                v.d = u.d+1
                fila.append(v)
                if v.valor == r.valor:
                    return v.d

while True:
    try:
        n, m = map(int, input().split())

        grafo = {}
        vertices = {}

        for i in range(m):
            a, b = map(int, input().split())

            if a not in vertices:
                vertices[a] = Vertice(a)
            if b not in vertices:
                vertices[b] = Vertice(b)

            va = vertices[a]
            vb = vertices[b]

            criar_grafo(grafo, va, vb)
        
        c, r, e = map(int, input().split())

        for v in vertices.values():
            v.d = 0

        distancia = bfs(grafo, vertices[c], vertices[r], e)
        print(distancia)

    except EOFError:
        break
                

