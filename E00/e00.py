
products = {}
n_products = int(input()) # quantidade de produtos a serem cadastrados

# Cadastro dos produtos
for i in range(n_products):
  line = input().split() # Leitura do código do produto e o preço por quilograma
  
  # Se o código do produto não estiver entre as chaves do meu dicionário eu adiciono o novo código
  if line[0] not in products: 
    products[line[0]] = float(line[1]) # adiciona [código]: preço no dict
  else:
    print(f"Produto com código {line[0]} já cadastrado.") 


while True:

  n_purchases = int(input()) # quantidade de compras
  
  # se quantidade de item a ser comprado == -1, encerra as compras.
  if(n_purchases == -1):
    break
  
  saldo = 0 # variável acumuladora do valor da compras

  for i in range(n_purchases):
    line  = input().split() # Leitura do código do produto e peso(kg)
    
    # se o código estiver no conjunto de chaves do dicionário ele pega o valor da respectiva chave(preço/kg), multiplica pelo peso(kg) e soma ao saldo da compra
    if line[0] in products: 
      saldo += float(line[1]) * products[line[0]]
    else:
     print(f"Produto com código {line[0]} não cadastrado.")
      
  # Exibição do saldo
  print(f"R${saldo:.2f}") 

    