classificacao = ['Ana', 'Carlos', 'Pedro']
print(classificacao )

nome_errado = input('Digite o nome do corredor que está com o nome errado: ')
nome_correto = input('Digite o nome correto do corredor: ')

posicao = classificacao.index(nome_errado)
print(posicao)
classificacao[posicao] = nome_correto
print(f"O nome {nome_errado} foi substituído por {nome_correto}.")
print(f"Lista atualizada: {classificacao}")