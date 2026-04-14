from collections import deque

# branco = 0
# cinza  = 1
# preto  = 2

class vertice:
    def __init__(self, nome):
        self.nome = nome
        self.cor = 0
        self.d = 0
        self.pre = None

    def print_v(self):
        print(self.nome)

def bfs(grafo, s):
    
    s.cor = 1
    s.d = 0
    s.pre = None

    fila = deque([s])
    arestas = []

    while fila:
        u = fila.popleft()
        for v in grafo[u]:
            if v.cor == 0:
                v.cor = 1
                v.d = u.d + 1
                v.pre = u.nome
                fila.append(v)
                arestas.append((u.nome, v.nome))
        u.cor = 2
    print("Arvore BFS gerada:")
    print(arestas)

    print(f"Distancia de {s.nome} até cada vértice:")
    for v in grafo:
        print(f"{v.nome} -> {v.d}")

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

# grafo = {
#     a:[b, d],
#     b:[e],
#     c:[e, f],
#     d:[b],
#     e:[d],
#     f:[f]
# }

bfs(grafo, c)