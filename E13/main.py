from collections import deque


def bsf(graph, s_vertice, t_vertice, path):
    """Função responsável por encontrar caminhos de s_vertice até t_vertice"""

    # conjunto de vertices visitados
    visited = set()
    queue = deque()
    queue.append(s_vertice)
    visited.add(s_vertice)
    path[s_vertice] = -1

    while queue:
        u = queue.popleft()  # remove do inicio da lista (complexidade O(1))

        # percorre as adjacências de u
        for u_adj, cap in graph[u].items():
            # só segue se houver capacidade residual > 0 e não tiver visitado
            if cap > 0 and u_adj not in visited:
                queue.append(u_adj)
                visited.add(u_adj)
                path[u_adj] = u
                # Chegamos ao vertice de chegada (t_vertice)
                if u_adj == t_vertice:
                    return True
    return False


def ford_fulkerson(graph, source, t_sink):
    """Função responsável por calcular o fluxo máximo de grafo direcionado"""

    max_flow = 0
    path = [-1] * (t_sink + 1)  # lista fixa, utiliza t_sink pois t_sink = n_computers

    # Enquanto houver caminho de s a t no grafo residual, roda o loop.
    while True:

        for i in range(1, t_sink + 1):
            path[i] = -1

        # se não há caminhos válidos no grafo residual, para.
        if not bsf(graph, source, t_sink, path):
            break

        # path_flow inicia com infinito
        path_flow = float("Inf")

        # começamos do vertice de chegada (t_sink)
        s = t_sink

        # enquanto s não for o vertice inicial, continua.
        while s != source:
            pai_s = path[s]
            # pegar a aresta cujo tem a menor capacidae
            path_flow = min(path_flow, graph[pai_s][s])
            s = pai_s

        # Adiciona o menor fluxo encontrado no caminho de s a t, no fluxo total.
        max_flow += path_flow

        # Atualiza as capacidades residuais das arestas
        # tanto originais quanto as reversas ao longo do caminho
        v = t_sink
        while v != source:
            pai_v = path[v]

            # Atualiza a aresta (pai_v -> v): diminuir capacidade para aumentar o fluxo, pois está aresta existe no grafo original
            graph[pai_v][v] -= path_flow

            # Atualiza (ou cria) a aresta reversa (v-> pai_v): nesse caso aumenta a capacidade, estamos reduzindo o fluxo.
            # As arestas reversas permite desfazer escolhas ruins

            # cria aresta inversa
            if pai_v not in graph[v]:
                graph[v][pai_v] = 0

            graph[v][pai_v] += path_flow

            # avança caminho (voltanto até chegar em s)
            v = pai_v

    return max_flow


def main():
    """Para este algoritmo será necessário termos o algorimo BFS para fornecer os caminhos de s a p no grafo residual"""
    n_computers, m_cables = map(int, input().split())

    # grafo dicionário de dicionários
    adj_dict = {}
    for _ in range(m_cables):
        u, v, c = map(int, input().split())

        # Se a chave não estiver presente no dic, cria uma e atribui uma lista vazia(list adj)
        if u not in adj_dict.keys():
            adj_dict[u] = {}
        if v not in adj_dict.keys():
            adj_dict[v] = {}

        adj_dict[u][v] = c

    max_flow = ford_fulkerson(adj_dict, 1, n_computers)
    print(max_flow)


if __name__ == "__main__":
    main()
