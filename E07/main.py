def main():
    n_reliquias = int(input()) 
    # Lista de estabilidades de cada reliquia, iniciando do mais embaixo ate o topo
    reliquias = map(int, input().split(' ')[:n_reliquias])
    for i in reliquias:
        print(i, end=' ')
  
if __name__ == "__main__":
    main()
    