# def fatorial(n):
#     if n == 0:  # Condição de Parada
#         return 1
#     return n * fatorial(n - 1)  # Chamada Recursiva
#
#
# print(fatorial(5))  # Saída: 120
#
# print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
#
# def multiplicador(n):  # Função externa
#     def multiplica(x):  # Closure
#         return x * n  # Usa a variável 'n' da função externa.
#     return multiplica  # Retorna a Função Interna
#
#
# triplo = multiplicador(3)
# valor = triplo(5)
# print(valor)  # Saída: 15
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")

lista_preco = [1500, 1000, 800, 2000]

def definir_taxa_imposto(preco):
    if preco > 1000:
        taxa = 0.15
    elif preco > 1500:
        taxa = 0.2
    else:
        taxa = 0.1
    return taxa


def calcular_imposto(lista_valores):
    imposto_total = 0
    for preco in lista_valores:
        taxa_imposto = definir_taxa_imposto(preco)
        imposto = preco * taxa_imposto
        imposto_total = imposto_total + imposto
    return imposto_total

calcular_imposto(lista_preco)
print(calcular_imposto(lista_preco))

lista2_preco = [500, 4000,3200,2600, 1000]
imposto_total = calcular_imposto(lista2_preco)
print(imposto_total)

print("*-*-*-*-*-*-*-*-*-*-*-*-*-*")
