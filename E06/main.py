import math 


def cross_product(a, b, p):
    """Retorna o produto vetorial 2D (área orientada) de AB x AP."""
    return (b[0]- a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])


def point_line_distance(a, b, p):
    """Calcula a distância perpendicular de um ponto P à reta que passa por A e B."""

    # Para realizar o cálculo da distância de um ponto à uma reta, utiliza-se o conceito da área do paralelogramo,
    # quanto maior a distância do ponto, maior a área do paralelogramo (Área do pararelogramo = || AP * AB ||).
    return abs(cross_product(a, b, p))    


def is_right_point(a, b, p):
    """Retorna True se p estiver à direita da reta orientada AB."""
    return (cross_product(a, b, p) < 0)

def all_points_is_colinear(points, a, b):
    for p in points:
        # Prod vetorial (Determinante)
         cross = (b[0]- a[0]) * (p[1] - a[1]) - (b[1] - a[1]) * (p[0] - a[0])
         
         # Achou um ponto fora da reta (reta que passa nos pontos A e B), ou seja, um ponto que não seja colinear.
         if abs(cross) > 0:
             return False
    # Retorna true para quando todos os pontos são colineares entre si, ou seja, todos os determinantes entre dois pontos
    # tem valor igual a zero.
    return True

def quick_hull(points):
    a = min(points, key=lambda p:p[0]) # Ponto mais a esquerda do conjunto de pontos (menor x)
    b = max(points, key=lambda p:p[0]) # Ponto mais a direita do conjunto de pontos (maior x)
    
    # Caso especial: todos os pontos são colineares entre si, retorna o conjunto de pontos ordenados 
    if all_points_is_colinear(points, a, b):
        # Ordena em ordem crescente por Ei, caso empate ordena pelo menor Vi
        return sorted(points)
    
    # Caso geral 
    s1 = [p for p in points if is_right_point(a, b, p)] # Pontos à direita da reta (a,b)
    s2 = [p for p in points if is_right_point(b, a, p)] # Pontos à direita da reta (b,a)

    # Concatena todos os pontos (pontos A, B e os pontos retornados de Hull_set para os conjuntos S1 e S2)
    return [a] + hull_set(s1, a, b) + [b] + hull_set(s2, b, a)
   
def hull_set(points, p, q):
    # Caso base: não possui mais nenhum ponto 
    if not points: 
        return []
    
    # c é o ponto mais distante da reta pq, dado o conjunto de pontos, verificamos o mais distante.
    # A função max percorre todos os pontos aplica em cada um deles na função e retorna o elemento que teve o maior valor retornado (maior dist) pela função
    c = max(points, key= lambda point:point_line_distance(p, q, point))
    
    
    s1 = [pt for pt in points if is_right_point(p, c, pt)] # Pontos a direita da reta (p, c)
    s2 = [pt for pt in points if is_right_point(c, q, pt)] # Pontos à direita da reta (c, q)

    return hull_set(s1, p, c) + [c] + hull_set(s2, c, q)


def print_saida(casoT, n_stones, coordinate_convex_hull):
    print(f"Caso {casoT}:\nTamanho do colar: {n_stones}\nPedras ancestrais: ",end='')
    for i,(e_i, v_i) in enumerate(coordinate_convex_hull):
        print(f"({e_i:.4f},{v_i:.4f})",  end='')  
        
        # Se não for o último elemento colocamos vírgula para separar entre as coordenadas
        if i < n_stones - 1:
            print(',', end='')
    print("\n")
    
    
def main():
    
    t_testes = int(input())
    for i in range(t_testes):
        coordinates = [] # Array que guarda os pontos de coordenadas (Ei, Vi)
        result = [] # Array que guarda os pontos do envoltório convexo
        
        n_stones = int(input())
        for _ in range(n_stones):
            line = input().split()
            e_i = float(line[0])
            v_i = float(line[1])
            coordinates.append((e_i, v_i))
            
        result = quick_hull(points=coordinates)
        print_saida(i+1, len(result), result)
    
    
    
if __name__ == "__main__":
    main()
