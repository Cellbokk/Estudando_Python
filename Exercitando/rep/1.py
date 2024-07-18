while True:
    try:
        nota = float(input("Digite uma nota entre 0 e 10: "))
        if 0 <= nota <= 10:
            print(f"Você digitou uma nota válida: {nota}")
            break
        else:
            print("Nota inválida. Por favor, digite uma nota entre 0 e 10.")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")