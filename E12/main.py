import heapq


def print_saida(cost, mst, required_condition=False):
    """Funcao responsável por formatar a saída"""

    print(f"Custo minimo: {cost}\nPontes reconstruidas:")
    # Ordena por peso de aresta
    for u, v, _ in sorted(mst, key=lambda x: x[2]):
        print(f"{u} - {v}")
    print()


def prim_algorithm(adj_dic, start):
    """Algoritmo guloso - Prim"""

    # Lista de prioridade para armazenar as arestas com seus respectivos pesos
    pq = []
    # Cria um array único de vertices visitados
    visited = set()
    # Variável que armazena o custo total da MST
    total_cost = 0
    # arestas da MST
    mst_edges = []

    # começa com o primeiro vertice
    visited.add(start)
    for v, wt in adj_dic[start]:
        heapq.heappush(pq, (wt, start, v))

    # Armazena o peso da aresta anterior, inicializa com None.
    prior_wt = None

    # Enquanto a fila de prioridade não for vazia, executa while.
    while pq:

        # peso, origem, destino
        wt, u, v = heapq.heappop(pq)
        # Detecta arestas cujo tem pesos iguais, caso tenha retorna 0 e uma lista vazia
        if prior_wt is not None and wt == prior_wt:
            return 0, []
        # Peso da aresta anterior recebe o peso da aresta atual
        prior_wt = wt

        # Se o vertice já foi visitado, pula ele.
        if v in visited:
            continue

        # Incrementa com peso da aresta ao custo total
        total_cost += wt
        # Insere a aresta cujo tem o menor peso na mst
        mst_edges.append(tuple(sorted([u, v])) + (wt,))
        # Insere o vertice (v) no array de visitados, para evitar ciclos.
        visited.add(v)

        # verifica os vertices adjacentes
        for v_adj, wt in adj_dic[v]:
            if v_adj not in visited:
                # adiciona arestas que estão conectadas ao vertice
                heapq.heappush(pq, (wt, v, v_adj))

    return total_cost, mst_edges


def main():
    # Numeros de casos
    x_cases = int(input())
    for _ in range(x_cases):
        # Numeros de vertices(acampamentos), numeros de arestas(pontes)
        n_vertices, m_edges = map(int, input().split())
        # Create adjacency dict
        adjacency_dict = {}
        for _ in range(m_edges):
            u, v, wt = map(int, input().split())

            # Se o vertice ainda nao existe no dict cria uma chave e atribui uma lista vazia []
            if u not in adjacency_dict.keys():
                adjacency_dict[u] = []

            if v not in adjacency_dict.keys():
                adjacency_dict[v] = []

            adjacency_dict[u].append((v, wt))
            adjacency_dict[v].append((u, wt))

        # Escolhe o primeiro vértice arbitrariamente
        start = next(iter(adjacency_dict))

        # Requisito para ter um MST - Minimum Spanning Tree
        # Num de aresta é igual ao numero de vertices - 1 (|E'| = |V| - 1)
        if m_edges >= n_vertices - 1:
            cost, mst = prim_algorithm(adjacency_dict, start)
            # Se cost > 0, ou seja, nao possui arestas de pesos iguais e quantidade de aresta atende o requisito, printa saida.
            if cost != 0 and len(mst) >= n_vertices - 1:
                print_saida(cost, mst)
            elif cost == 0:
                print("Esse nao e o caminho correto para a Cidade Perdida de Z.\n")
            else:
                print(f"O vale nao pode ser completamente atravessado.\n")
        else:
            print(f"O vale nao pode ser completamente atravessado.\n")


if __name__ == "__main__":
    main()
