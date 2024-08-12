import numpy as np

precos_acoes = np.array([
    [150, 200, 180, 220, 170], 
    [155, 205, 185, 225, 175], 
    [160, 210, 190, 230, 180],
    [165, 215, 195, 235, 185], 
    [170, 220, 200, 240, 190], 
    [175, 225, 205, 245, 195], 
    [180, 230, 210, 250, 200]
])

media_precos = np.mean(precos_acoes, axis=0)

print("Média diária dos preços das ações para cada empresa ao longo da semana:")
print(media_precos)

variacao_precos = np.max(precos_acoes, axis=0) - np.min(precos_acoes, axis=0)

print("Variação diária das ações para cada empresa ao longo da semana:")
print(variacao_precos)

precos_B = precos_acoes[:, 1]
dia_maior_preco = np.argmax(precos_B)
dia_menor_preco = np.argmin(precos_B)

print("Dia da semana em que a ação da empresa B teve o maior preço:", dia_maior_preco + 1)
print("Dia da semana em que a ação da empresa B teve o menor preço:", dia_menor_preco + 1)

novos_precos_acoes = precos_acoes * 1.05
nova_media_precos = np.mean(novos_precos_acoes, axis=0)

print("Matriz de preços das ações atualizada após aumento de 5%:")
print(novos_precos_acoes)
print("\nNova média diária dos preços das ações para cada empresa:")
print(nova_media_precos)
