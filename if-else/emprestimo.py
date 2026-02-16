renda_mensal = float(input("Digite a renda mensal: R$ "))
emprestimo_parcela = float(input("Digite a da parcela desejada: R$ "))

if renda_mensal > 2000 and emprestimo_parcela <= 0.3 * renda_mensal:
    print("Empréstimo aprovado!")
elif  renda_mensal <= 2000:
    print("Empréstimo negado: renda insuficiente.")
else:
    print("Empréstimo negado: parcela acima de 30% da renda.")
