from collections import deque

# branco = 0
# cinza  = 1
# preto  = 2

class vertice:
    def __init__(self, nome):
        self.nome=nome
        self.d = 0
        self.f = 0
        self.p = None
        self.cor=0

    def print_v(self):
        print(self.nome)

def dfs(grafo):
    tempo=0
    arestas = []
    for u in grafo:
        if u.cor == 0:
            dfs_visit(grafo, u, tempo)
        arestas.append((u.nome, u.p))
    
    print(arestas)

def dfs_visit(grafo, u, tempo):
    tempo+=1
    u.d=tempo
    u.cor=1
    for v in grafo[u]:
        if v.cor==0:
            v.p=u.nome
            dfs_visit(grafo, v, tempo)
    u.cor=2
    tempo+=1
    u.f=tempo

a = vertice('a')
b = vertice('b')
c = vertice('c')
d = vertice('d')
e = vertice('e')
f = vertice('f')


grafo = {
    a:[d, f],
    b:[e],
    c:[e, f],
    d:[a],
    e:[b, c, f],
    f:[c, e]
}

dfs(grafo)