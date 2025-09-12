class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False          # booleano: marca fim de palavra


def insert(root, word):
    current = root # Nó atual
    for c in word.strip():
        idx = ord(c) - ord('A')
        #Se posição estiver vazia, cria-se um nó com a respectiva letra
        if current.children[idx] is None:
            current.children[idx] = TrieNode()
        current = current.children[idx]
    current.isEnd = True         # marca que esta posição termina uma palavra


def search_direction(grid, x, y, dx, dy, node, path, found_words):
    lines, cols = len(grid), len(grid[0])

    # Condição de parada
    if not (0 <= x < lines and 0 <= y < cols):
        return

    idx = ord(grid[x][y]) - ord('A')
    if node.children[idx] is None:
        return

    node = node.children[idx]
    path += grid[x][y]

    # Se chegou ao final de um palavra na trie e ela está no grid, então adiciona em found_words
    if node.isEnd:
        found_words.add(path)


    search_direction(grid, x + dx, y + dy, dx, dy, node, path, found_words)


# Driver Code
if __name__ == '__main__':

    line_one = input().split(' ')

    lines = int(line_one[0])  # Quantidade de linhas
    columns = int(line_one[1])  # Quantidade de caracteres

    # Lista de palvras encontradas no grid
    found_words = set()

    grid = []

    # Leitura das letras do grid
    for i in range(lines):
        columns_words = input()
        grid.append(columns_words[:columns])

    n_words = int(input())  # número de palavras no dicionario

    root = TrieNode() # Inicializa a trie com uma raiz vazia

    # Leitura das palavras do dicionario
    for j in range(n_words):
        word = input()
        if 2 <= len(word) <= 25:
            insert(root, word) # insere na trie

    # Possiveis direções
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0),
        (1, 1), (-1, -1), (1, -1), (-1, 1)
    ]

    for i in range(lines):
        for j in range(columns):
            for dx, dy in directions:
                search_direction(grid, i, j, dx, dy, root, "", found_words)

    print(len(found_words))
    for word in sorted(found_words):
        print(word)
