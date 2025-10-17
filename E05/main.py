"""
Uma inversão ocorre quando os índices
i < j, porém v[i] > v[j]
"""

# função responsável por realizar a intercalação (Conquistar e juntar) entre os dois subvetores de vec e contabilizar as inversões  
def intercalaCountInv(vec, p, q, r, aux):

    """
    Intercala vec[p:q] e vec[q:r] em ordem crescente e conta inversões.
    Usa array auxiliar 'aux' (pré-alocado) para armazenar os valores de maneira ordenada.
    """
    
    i = p # Ponteiro da esquerda
    j = q # Ponteiro da direita
    k = p # Ponteiro auxiliar 
    n_inv = 0 # Numero de inversões 

    # Condição do while para garantir que não extrapole os índices do vetor
    while i < q and j < r:
        if vec[i] <= vec[j]:
            aux[k] = vec[i]
            i+=1
        # Nesse caso do else a inversão ocorre, pois i < j, porém v[i] >= v[j]
        else: 
            aux[k] = vec[j]
            j+=1
            n_inv+= (q - i) # todos os elementos restante à esquerda são inversões 
        k += 1
        # Copia o restante da esquerda
    while i < q:
        aux[k] = vec[i]
        i += 1
        k += 1

    # Copia o restante da direita
    while j < r:
        aux[k] = vec[j]
        j += 1
        k += 1
        
    # Copia de volta para o vetor original, agora já ordenado 
    for t in range(p, r):
        vec[t] = aux[t]

    return n_inv
        
# função mergeSortCountInv - Realiza a quebra do array vec em partes menores (dividir) até chegar no caso base
# A qual depois irá subir na recursão realizando a intercalação e verificação de inversões 

def mergeSortCountInv(vec, p, r, aux):
    if r - p <= 1:
        return 0
    q = (p + r) // 2 # Realiza uma divisão inteira
    
    n_inv = 0
    n_inv += mergeSortCountInv(vec,p, q, aux) # parte esquerda do vetor
    n_inv += mergeSortCountInv(vec, q, r, aux) # parte direita do vetor 
    n_inv += intercalaCountInv(vec, p, q, r, aux) # Intercala e verifica as inversções 

    return n_inv

def main():
    
    n_trechos = int(input()) 
    trechos = [] # Lista de tuplas (trecho - T, contabiliza as inversões  qtd de ultrapassagens - U)
    pilotos = [] # Lista de tuplas [(s0,sf), (s1,sf1)...()] - posicao inicial e posicao final de cada jogador
    posi_final = [] # Lista que guarda apenas a posicao final de cada jogador (Array que iremos verificar as inversões)

    for i in range(n_trechos):
        
        n_players = int(input()) 
    
        pilotos.clear() # Zera o array de pilotos para cada trecho
        posi_final.clear() # Zera o array de posições finais para cada trecho 
        
        for _ in range(n_players):
            s0, sf = input().split(' ')
            # Os valores s0 e sf estão em string, converte para int.
            s0 = int(s0)
            sf = int(sf) 
            pilotos.append((s0,sf)) 
        
        # Ordena o vetor de pilotos em ordem crescente de largadas
        pilotos.sort(key = lambda x: x[0])
        
        # Adiciona os tempos finais dos jogadores no array de posições finais
        for s0, sf in pilotos:
            posi_final.append(sf)

        # cria aux pré-alocado do tamanho do vetor que será ordenado
        aux = [0] * len(posi_final)
        
        # Verifica a quantidade de ultrapassagens, contando a quantidade de inversões no array posi_final
        qtd_U = mergeSortCountInv(posi_final, 0, len(posi_final), aux)
        trechos.append((i, qtd_U))
        
    # Imprime resultado de maneira decrescente de ultrapassagens - do maior U para o menor U
    for i,u in sorted(trechos, key=lambda x:x[1], reverse=True):
        print(i,u)
        
if __name__ == "__main__":
    main()
