
produtos = {}

print("Por favor, insira o nome e o preço de cinco produtos:")

for i in range(5):
    print(f"\nProduto {i + 1}:")
    nome_produto = input("Nome do produto: ")
    
    
    while True:
        try:
            preco_produto = float(input("Preço do produto: R$ "))
            if preco_produto < 0:
                print("O preço não pode ser negativo. Por favor, insira um valor válido.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número para o preço.")
            

    produtos[nome_produto] = preco_produto


total_compra = 0
for preco in produtos.values():
    total_compra += preco


print("\n--- Resumo da Compra ---")
print("Produtos e Preços:")
for nome, preco in produtos.items():
    print(f"- {nome}: R$ {preco:.2f}")

print(f"\nValor total da compra: R$ {total_compra:.2f}")