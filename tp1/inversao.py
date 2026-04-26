import sys
from collections import deque

class Vertice:
    def __init__(self, v, d):
        self.v=v
        self.d=d

def inverter(v):
    return int(str(v)[::-1])

def bfs(a, b):
    visitados = set()
    fila = deque([Vertice(a, 0)])

    visitados.add(a)

    while fila:
        u = fila.popleft()

        if u.v == b:
            return u.d

        v1 = u.v + 1
        if v1 not in visitados:
            visitados.add(v1)
            fila.append(Vertice(v1, u.d + 1))

        v2 = inverter(u.v)
        if v2 not in visitados:
            visitados.add(v2)
            fila.append(Vertice(v2, u.d + 1))

dados = list(map(int, sys.stdin.read().split()))

if not dados:
    sys.exit()

t = dados[0]
idx = 1

for i in range(t):
    a = dados[idx]
    b = dados[idx + 1]
    idx += 2

    print(bfs(a, b))

