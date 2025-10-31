import math
import heapq

def prioridade_do_par(a, b, priority):
    """Funcao resposavel por retornar o par mais prioritario"""
    return min(priority[a], priority[b])


def distance_between_two_points(pointA,pointB):
    """Funcao que calcula a distância entre dois pontos"""
    return math.sqrt((pointA[0] - pointB[0])**2 + (pointA[1] - pointB[1])**2)

def brute_force_closest_pair(P, n, priority):
    """Força bruta com desempate por prioridade do par."""
    min_d = float('inf')
    pair = None
    for i in range(n):
        for j in range(i+1, n):
            dist = distance_between_two_points(P[i][1:], P[j][1:])
            # Se encontrou distância menor OU empate com prioridade melhor
            if (dist < min_d) or (abs(dist - min_d) < 1e-9 and
                                  prioridade_do_par(P[i][0], P[j][0], priority) <
                                  prioridade_do_par(pair[0], pair[1], priority)):
                min_d = dist
                # ordena os ids de acordo com prioridade (menor índice primeiro)
                if priority[P[i][0]] < priority[P[j][0]]:
                    pair = (P[i][0], P[j][0])
                else:
                    pair = (P[j][0], P[i][0])
    return min_d, pair


def closestPair(px, py ,n, priority):
    """Funcao responsavel por encontrar o par de pontos mais proximos utilizando divisao e conquista"""
    
    # Caso base - utiliza forca bruta para calcular o par de pontos mais proximos
    if n <= 3:
        return brute_force_closest_pair(px, n, priority)
    
    # divide no meio o conjunto de pontos 
    mid = n // 2 
    mid_x = px[mid][1]
    
    # conjuntos dos pontos x do lado esquerdo e direito, divide X conforme a linha do meio
    left_x = px[:mid] 
    right_x = px[mid:]
    
    # conjunto dos ponto y do lado esquerdo e direito, divide Y conforme a linha do meio
    left_y = [p for p in py if p[1]<= mid_x]
    right_y = [p for p in py if p[1] > mid_x]
    
    # ======== Conquista ========
    d_left, pair_left = closestPair(left_x, left_y, len(left_x), priority)
    d_right, pair_right = closestPair(right_x, right_y, len(right_x), priority)
    
    # desempate entre lados esquerdo/direito por prioridade do par, se distâncias iguais
    if (d_left < d_right) or (abs(d_left - d_right) < 1e-9 and 
                            prioridade_do_par(pair_left[0], pair_left[1], priority) <
                            prioridade_do_par(pair_right[0], pair_right[1], priority)):
        d = d_left
        best_pair = pair_left
    else:
        d = d_right
        best_pair = pair_right

        
    # ======== Combina (strip central) ========
    # Pega os pontos próximos à linha central (distância < d)
    strip = [p for p in py if abs(p[1] - mid_x) < d]

    # Verifica no máximo os próximos 7 vizinhos
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 7, len(strip))):
            d2 = distance_between_two_points(strip[i][1:], strip[j][1:])
            
            # Caso a distancia entre pares empate, utilize o criterio da prioridade
            if (d2 < d) or (abs(d2 - d) < 1e-9 and 
                          prioridade_do_par(strip[i][0], strip[j][0], priority) < prioridade_do_par(best_pair[0], best_pair[1], priority)):
                      
                d = d2
                # ordenar o par pelo id de maior prioridade primeiro
                if priority[strip[i][0]] < priority[strip[j][0]]:
                    best_pair = (strip[i][0], strip[j][0])
                else:
                    best_pair = (strip[j][0], strip[i][0])
                            
    return d, best_pair
                                      
def calculate_malha_essencial(systems, n_main_systems, tensao_max, priority):
    """Funcao que executa o algoritmo de prim, para encontrar a arvore geradora minima"""
    
    # Inicializacao do dicionario para acesso rapido as coordenadas 
    coordenadas = {}
    for id, x, y in systems:
        # id: (x,y)
        coordenadas[id] = (x,y)

    # Conjunto dos vértices já visitados, ou seja, estao na MST
    visited =  set()
    # malha final(MST) -  conjunto solucao
    malha_final = []
    # Fila de prioridade para as arestas
    pq = []
    # Começa com o sistema de maior prioridade, vertice inicial
    k = systems[0]
    # inicia como o
    visited.add(k[0]) 
    
    # adiciona as arestas do primeiro vertice à fila
    add_arestas_do_vertice_atual(k[0], coordenadas, visited, pq, tensao_max, priority)
    
    # loop guloso do prim - enquanto houver vertices nao visitados 
    while len(visited) < n_main_systems:
        # se fila está vazia precisamos remocomeçar em um novo componente
        if not pq:
            # escolhe o próximo vértice não visitado de maior prioridade
            for id, _, _ in systems:
                if id not in visited:
                    visited.add(id)
                    add_arestas_do_vertice_atual(id, coordenadas, visited, pq, tensao_max, priority)
                    break
        # Se ainda assim a fila estiver vazia, significa que não há conexões possíveis
        if not pq:
            break
        
        # retorna a aresta mais barata (com menor distancia) - escolha gulosa
        dist,_ ,id_origem, id_dest = heapq.heappop(pq) 
        
        # verifica se o novo vértice(destino) já está nos visitados, para evitar ciclos
        if id_dest in visited:
            continue
        
        # se não estiver adiciona nos visitados
        visited.add(id_dest)     

        # verifica a prioridade para adicionar na ordem correta na malha final
        if priority[id_origem] < priority[id_dest]:          
            malha_final.append((id_origem, id_dest, dist))
        else:
            malha_final.append((id_dest, id_origem, dist))
            
        # adiciona as novas arestas válidas
        add_arestas_do_vertice_atual(id_dest, coordenadas,visited, pq, tensao_max, priority)
        
    return malha_final
        
def add_arestas_do_vertice_atual(id_atual, coordenadas, visited, pq, tensao_max, priority):
    """Funcao responsavel por calcular os pesos das arestas a partir de um vertice atual"""
    
    # Pega as coordenadas do vertice atual
    coord_atual = coordenadas[id_atual]
    # itera sobre todos os vertices e calcula a distancia entre o vertice atual com todos os demais
    for id_vizinho, coord_vizinho in coordenadas.items():
        # Nao cria aresta para si mesmo ou para quem já está no conjunto solucao 
        if id_vizinho != id_atual and id_vizinho not in visited:
            dist = distance_between_two_points(coord_atual,coord_vizinho)
            print(f"id_atual:{id_atual} id_viz:{id_vizinho} dist:{dist}") #!remover
            # Se a distancia calcula esta dentro da margem maxima de distancia, add na lista de prioridade.
            if dist <= tensao_max:
                # Adiciona a aresta (distância,desempate pela prioridade do destino (id_vizinho) o que tiver menor valor -> mais prioritario, origem, destino)
                # na fila de prioridade
                heapq.heappush(pq, (dist, priority[id_vizinho], id_atual, id_vizinho))
                
def printar_saida(solutionSet, dist_min, pair):
    """Funcao responsavel por formatar a saida"""
    
    for id_origem, id_dest, dist in solutionSet:
        print(f"{id_origem}, {id_dest}, {dist:.2f}") 
    print(f"Ponto de Ressonância: {pair[0]}, {pair[1]}, {dist_min:.2f}",end='')
    print('\n')
    
def main():
    
    # Numero de problemas a serem resolvidos
    n_problems = int(input()) 
    for i in range(n_problems):
        # N° de sistemas(coordenadas), N° de sistemas mais importantes, Valor da tensão máxima (Valor máximo da distância entre dois pontos)
        n_systems, n_main_systems, tensao_max = map(int, input().split(' ')) 
        # Lista de tuplas, a qual representa os sistemas (id, x, y) 
        systems = [(id, float(x), float(y)) for id, x, y in (input().split(' ') for _ in range(n_systems))] 
        
        # Cria dicionário de prioridade 
        priority = {id: i for i, (id, _, _) in enumerate(systems)}

        # Parte 1 - Encontra a arvore geradora minima
        # Cria a malha de tuneis entres os sistemas mais importantes
        result = calculate_malha_essencial(systems[:n_main_systems], n_main_systems, tensao_max, priority) 
        # Parte 2 - encontra o par de pontos mais proximos do conjunto de vertices 
        # Encontra o ponto de ressonancia de um conjunto de pontos ordenados pelo x das coordenadas, ordenado pelo y das coordenadas
        dist_min, pair = closestPair(sorted(systems, key=lambda x:x[1]), sorted(systems, key=lambda x:x[2]), len(systems), priority)
        
        #Imprime saida, enviando os seguintes parâmetros:
        # Parâmetro 1: Malha ordenada, primeiramente pela distância, se for igual, desempata com a prioridade da id_origem, se for igual, por fim desempata com a prioridade do id_dest
        # Parâmetro 2: dist_min obtida da função que encontra o par de pontos mais proximos
        # Parâmetro 3: pares mais proximos obtido novamente da funcao closestPair
        printar_saida(sorted(result, key=lambda x: (x[2], priority[x[0]], priority[x[1]])), dist_min, pair)
        
        
if __name__ == "__main__":
    main()
