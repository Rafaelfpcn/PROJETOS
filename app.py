print("⚡ === Calculadora de Consumo Elétrico === ⚡")

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horasdia = float(input("Digite o tempo médio de uso diário em horas: "))

consumomensal = (potencia * horasdia * 30) / 1000
valorkwh = 0.75
custoestimado = consumomensal * valorkwh

print("\n📊 === Resultado ===")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumomensal:.2f} kWh/mês")
print(f" Custo estimado: R$ {custoestimado:.2f} por mês")