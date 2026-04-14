#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct No {
    int valor;
    struct No* prox;
} No;

typedef struct {
    int *dados;
    int inicio, fim;
} Fila;

void adicionar_no(No* g[], int x, int y) {
    No* novo = (No*) malloc(sizeof(No));
    novo->valor = y;
    novo->prox = g[x];

    g[x] = novo;
    novo = (No*) malloc(sizeof(No));

    novo->valor = x;
    novo->prox = g[y];
    g[y] = novo;
}


Fila* criar_fila(int n){
    Fila* f = (Fila*) malloc(sizeof(Fila));
    f->dados = (int*) malloc(n * sizeof(int));
    f->inicio = 0;
    f->fim = 0;
    return f;
}

void enqueue(Fila* f, int x) {
    f->dados[f->fim++] = x;
}
int dequeue(Fila* f) {
    return f->dados[f->inicio++];
}
bool vazia(Fila* f) {
    return f->inicio == f->fim;
}

void bfs(No* g[], int s, bool visitados[]) {
    Fila* fila = criar_fila(10000);
    enqueue(fila, s);
    visitados[s] = true;

    while (!vazia(fila)) {
        int no = dequeue(fila);
        No* atual = g[no];

        while (atual != NULL) {
            int n = atual->valor;
            if (!visitados[n]) {
                visitados[n] = true;
                enqueue(fila, n);
            }
            atual = atual->prox;
        }
    }
}

int main() {
    int t;
    scanf("%d", &t);

    char resultados[1000][100];
    
    for (int teste = 1; teste <= t; teste++) {
        
        int n, m;

        scanf("%d", &n);
        scanf("%d", &m);

        No* grafo[n+1];
        int i, j;
        for (i=1; i <= n; i++) {
            grafo[i] = NULL;
        }

        for (j=0; j < m; j++) {
            int x, y;
            scanf("%d %d", &x, &y);
            adicionar_no(grafo, x, y);
        }

        bool visitados[n+1];
        for (int i = 0; i <= n; i++) {
            visitados[i] = false;
        }

        int k = 0;

        for (int i = 1; i <= n; i++) {
            if (!visitados[i]) {
                bfs(grafo, i, visitados);
                k++;
            }
        }

        if (k == 1) {
            sprintf(resultados[teste-1], "Caso #%d: a promessa foi cumprida", teste);
        } else {
            sprintf(resultados[teste-1], "Caso #%d: ainda falta(m) %d estrada(s)", teste, k-1);
        }
    }
    int i;
    for (i= 0; i < t; i++) {
        printf("%s\n", resultados[i]);
    }

    return 0;
}


