from math import cos, sin, asin, sqrt, pi
import heapq


# Função responsavel por converter uma coordenada em graus para radianos
def convert_degree_to_radian(point):
    return point * (pi / 180)


# Função responsável por calcular a distância entre dois pontos na superficie
def haversine_formula(latC, lonC, lat_x, lon_y):
    earth_radius = 6371.0  # Raio da terra em kilômetros
    delta_phi = lat_x - latC
    delta_lambda = lon_y - lonC
    sqrt_expression = sqrt(sin(delta_phi / 2) ** 2 +
                           cos(latC) * cos(lat_x) *
                           sin(delta_lambda / 2) ** 2)

    d = 2 * earth_radius * asin(sqrt_expression)
    return d


players = int(input())

distances_players = []  # Inicializa a lista vazia que será nossa heap

point_values = input().split(' ')  # Pontos de [latitude e longitude]
latC = convert_degree_to_radian(float(point_values[0]))  # Latitude do ponto correto
lonC = convert_degree_to_radian(float(point_values[1]))  # Longitude do ponto correto

i = 0  # iterador
while i < players:
    # Leitura do nickname e dos pontos de latitude e longitude
    nickname, lat_x, lon_y = input().split(' ')
    lat_x = convert_degree_to_radian(float(lat_x))  # Converte para radianos o ponto de latitude
    lon_y = convert_degree_to_radian(float(lon_y))  # Converte para radianos o ponto de longitude
    result = haversine_formula(latC, lonC, lat_x, lon_y)  # Resultado do calculo da distancia

    # Using a priority queue
    heapq.heappush(distances_players, (result, nickname))  # insere um novo elemento na heap
    print(f"> [AVISO] MELHOR PALPITE: {distances_players[0][0]:.3f}km")  # acessa o menor elemento

    i += 1

# Saida do exercicio
print(f"\nRANKING\n-------")

for i, (distance, player) in enumerate(sorted(distances_players), start=1):
    result_message = f"{i:2}. {player:<20} : {distance:6.3f} km"

    if distance > 0.050:
        print(result_message)
    else:
        print(result_message + " [FANTASTICO]")
