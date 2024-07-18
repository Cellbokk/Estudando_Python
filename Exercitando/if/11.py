import os
salario = float(input("Digite seu salario:"))

if salario <= 280.00:
    aumento = salario * (20 / 100)
    novo_salario = salario + aumento
    os.system("clear")
    print("Como voce ganha 280 para baixo seu aumento e de 20%\n")
    print(f"Seu salario de {salario} com 20% agora e {novo_salario}")

elif salario >= 280.00 and salario <= 700.00:
    aumento = salario * (15 / 100)
    novo_salario = salario + aumento
    os.system("clear")
    print("Como voce ganha entre 280 a 700 reais terá um aumento de 15%")
    print(f"Seu salario de {salario} com 15% agora e {novo_salario}")

elif salario >=700.00 and salario <=1500.00:
    aumento = salario * (10 / 100)
    novo_salario = salario + aumento
    os.system("clear")
    print("Como voce ganha entre 700 a 1500 reais terá um aumento de 10%")
    print(f"Seu salario de {salario} com 10% agora e {novo_salario}")

elif salario > 1500.00:
    aumento = salario * (5 / 100)
    novo_salario = salario + aumento
    os.system("clear")
    print("Como voce ganha mais que 1500 reais terá um aumento de 5%")
    print(f"Seu salario de {salario} com 5% agora e {novo_salario}")

