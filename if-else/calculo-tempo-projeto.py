atividadeA = int(input("Digite o numero de dias da atividade A: "))
atividadeB = int(input("Digite o numero de dias da atividade B: "))
atividadeC = int(input("Digite o numero de dias da atividade C: "))

# if atividadeA > atividadeB and atividadeA > atividadeC:
#     print(f"A atividade A levou mais tempo do que as outras duas.")
# elif atividadeB > atividadeA and atividadeB > atividadeC:
#     print(f"A atividade B levou mais tempo do que as outras duas.")
# else:
#     print("Os dias não podem ser negativos")

if (atividadeA >= 0 and atividadeB >= 0 and atividadeC >= 0):
    tempo_total = atividadeA + atividadeB + atividadeC
    print(f"O tempo total do projeto é de {tempo_total} dias.")
else:
    print("Erro: Os dias não podem ser negativos.")