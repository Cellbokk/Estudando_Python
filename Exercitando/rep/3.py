def validar_nome():
    while True:
        nome = input("Digite seu nome (maior que 3 caracteres): ").strip()
        if len(nome) > 3:
            return nome
        else:
            print("Nome inválido. Deve ser maior que 3 caracteres.")

def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade (entre 0 e 150): "))
            if 0 <= idade <= 150:
                return idade
            else:
                print("Idade inválida. Deve ser entre 0 e 150.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def validar_salario():
    while True:
        try:
            salario = float(input("Digite seu salário (maior que zero): "))
            if salario > 0:
                return salario
            else:
                print("Salário inválido. Deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

def validar_sexo():
    while True:
        sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").strip().lower()
        if sexo in ['f', 'm']:
            return sexo
        else:
            print("Sexo inválido. Deve ser 'f' ou 'm'.")

def validar_estado_civil():
    while True:
        estado_civil = input("Digite seu estado civil ('s' para solteiro(a), 'c' para casado(a), 'v' para viúvo(a), 'd' para divorciado(a)): ").strip().lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        else:
            print("Estado civil inválido. Deve ser 's', 'c', 'v' ou 'd'.")

# Função principal
def main():
    nome = validar_nome()
    idade = validar_idade()
    salario = validar_salario()
    sexo = validar_sexo()
    estado_civil = validar_estado_civil()

    print("\nInformações Validadas:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Salário: R${salario:.2f}")
    print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
    print(f"Estado Civil: {'Solteiro(a)' if estado_civil == 's' else 'Casado(a)' if estado_civil == 'c' else 'Viúvo(a)' if estado_civil == 'v' else 'Divorciado(a)'}")

if __name__ == "__main__":
    main()
