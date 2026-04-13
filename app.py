excelente = 0
bom = 0
ruim = 0

for i in range(1, 51):
    print(f"\nEntrevistado {i}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("Opinião sobre o atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite a opção (1, 2 ou 3): "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        bom += 1
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida!")

# Resultado final
print("\n--- RESULTADO DA PESQUISA ---")
print(f"Quantidade de EXCELENTE: {excelente}")
print(f"Quantidade de RUIM: {ruim}")
