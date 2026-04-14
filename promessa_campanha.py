from collections import deque 

def adicionar_no(g, x, y):
    g[x].append(y)
    g[y].append(x)    
    
def bfs(g, s, visitados):
    fila = deque([s])
    visitados[s] = True

    while fila:
        no = fila.popleft()
        for n in g[no]:
            if not visitados[n]:
                visitados[n] = True
                fila.append(n)

t = int(input())

resultados = []
for teste in range(1, t+1):
    n = int(input())
    m = int(input())

    grafo = {}
    for no in range(1, n+1):
        grafo[no] = []
    
    for j in range(m):
        x, y = map(int, input().split())
        adicionar_no(grafo, x, y)

    visitados = [False for i in range(n+1)]
    k = 0

    for i in range(1, n+1):
        if not visitados[i]:
            bfs(grafo, i, visitados)
            k+=1

    if k == 1:
        resultados.append(f"Caso #{teste}: a promessa foi cumprida")
    else:
        resultados.append(f"Caso #{teste}: ainda falta(m) {k-1} estrada(s)")

for r in resultados:
    print(r)