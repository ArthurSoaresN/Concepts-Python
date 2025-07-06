n = int(input()) 
total_compra = 0.0
produtos_no_carrinho_saida = [] 

for _ in range(n):
    linha_produto = input() 
    partes = linha_produto.rsplit(' ', 1) 
    
    nome_produto = partes[0]
    preco_str = partes[1]   
    
    preco_produto = float(preco_str)
    total_compra += preco_produto
    produtos_no_carrinho_saida.append(f"{nome_produto}: R${preco_produto:.2f}")

for produto_formatado in produtos_no_carrinho_saida:
    print(produto_formatado)

print(f"Total: R${total_compra:.2f}")

#Entrada
"""
2
Pão 3.50
Leite 4.00
"""

#Saida
"""
Pão: R$3.50
Leite: R$4.00
Total: R$7.50
"""