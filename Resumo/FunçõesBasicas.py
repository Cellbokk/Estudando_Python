# Adição
print(5+23)

# Subtração
print(100-25)

# Multiplicação
print(5*10)

# Potência/Exponente
# o operador ** é equivalente ao expoente
print(5**2)

# 5*5 = 5^2 = 5**2 
print(5*5)


# Divisão (float)
# Retornar o valor decimal real da divisão
print(36/4)
print(10/3)         

# Divisão (int)
# Retornar um int. Se o quociente real for um valor decimal, apenas um número inteiro irá retornar
print(10//3)
print(19//6)

# Divisão Modular: retornar o restante da divisão
print(10%3)

# Operações com Strings e Caracteres
print("foo" * 5)
print('x'*3)

# ERRO: não pode concatenar um int com uma string --> necessidade de computar int com uma string
#print("hello" + 5)
# Fix
print("hello " + str(5))
# Adição de String = concatenação
print("hello " + "world")

# Comparadores em Strings
print("hello" < "world")
print("hello" == "world")
print("hello" > "world")

print("hello" == "hello")

print("cat" < "dog")

def switcher(number):
    # Use dicionário para armazenar switch cases
    # Se não for encontrado, o get() será o valor padrão
    return {
        '0': "Entered 0",
        '1': "Entered 1",
        '2': "Entered 2",
        '3': "Entered 3",
        '4': "Entered 4",
        '5': "Entered 5",
        '6': "Entered 6",
        '7': "Entered 7",
        '8': "Entered 8",
        '9': "Entered 9",
    }.get(number, "Invalid number!")

# input() lê uma entrada do usuário de stdin
number = input("Dial a number")
# Exibe o resultado da função switcher
print(switcher(number))

number = input("Dial a number")

if number == '0':
    print("Entered 0")
elif number == '1':
    print("Entered 1")
elif number == '2':
    print("Entered 2")
elif number == '3':
    print("Entered 3")
elif number == '4':
    print("Entered 4")
elif number == '5':
    print("Entered 5")
elif number == '6':
    print("Entered 6")
elif number == '7':
    print("Entered 7")
elif number == '8':
    print("Entered 8")
elif number == '9':
    print("Entered 9")
else:
    print("Invalid number!")

.strip()
#Remove espaços em branco (ou outros caracteres especificados) do início e do fim da string.
.upper()
#Converte todos os caracteres da string para maiúsculas.
.lower()
#Converte todos os caracteres da string para minuscula.