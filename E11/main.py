from Stack import Stack

def dfs_iterativo(adj, qtd_nos):
    """Executa o DFS iterativo em uma lista de adjacências usando pilha"""
    
    # Cria um array booleano para cada no tem tamanho qtd_nos + 1, pois a indexação incia em 1.
    visited = [False] * (qtd_nos + 1)
    # contador de componentes (ou seja moléculas)
    count_components = 0
    
    # Percorre todos os vertices (1,..,n)
    for v in range(1, qtd_nos + 1):
        # se v já foi visitado, signigica que ja esta em um componente
        if not visited[v]:
            stack = Stack()
            stack.push(v) # Adiciona na pilha
            componente = [] # componente a ser formada (molécula)
        
            while not stack.is_empty():
                no = stack.pop()
                # Se o no não foi visitado, marca como visitado e add no conjunto de componente(molécula)
                if not visited[no]:
                    visited[no] = True
                    componente.append(no)
                    #empilha vizinhos ainda nao visitados para explorar em profundidade 
                    for viz in adj[no]:
                        if not visited[viz]:
                            stack.push(viz)
            
            count_components += 1
    
    return count_components

def main():
    x_tests = int(input())
    for _ in range(x_tests):
        # n° de nós e n° de areas
        n_atomos, m_lig_qui  = map(int, input().split())
        # cria lista de adjacências, iniciando do nó 1.
        adj = [[] for _ in range(n_atomos + 1)]
        # montagem da lista de adjcência
        for _ in range(m_lig_qui):
            u,v = map(int, input().split(' '))
            adj[u].append(v)
            adj[v].append(u)
        # Conjuntos das moléculas(componentes)
        count_components = dfs_iterativo(adj, n_atomos)
        print(count_components)
        
if __name__ == "__main__":
    main()