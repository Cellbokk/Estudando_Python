for i in range(10):
    print(i)

print("\n")

#X começa a repetir de 2 e vai ate 9 por que começa com 0 
for x in range(2, 10):
    print(i)

print("\n")

for i in range(0, 10, 3):
    print(i)

print("\n")

for i in "hello!":
    print(i)

print("\n")

#define uma string "Hello World!"
string = "hello world!"
#O loop começa com 0 e depois ve o tamanho da string (que no caso e 12) e vai ir de 2 em 2
for i in range(0, len(string), 2):
    #o índice atual, convertido para string + uma string normal + o caractere na posição i da string
    print(str(i) + "th letter is "+ string[i])

print("\n")

count = 0
while (count < 10):
    print(count)

    # IMPORTANTE!!! Atualize o contador!
    count += 1

print("\n")

while True:
  user = input("Enter something to be repeated: ")

  if user=="end":
    print("Terminate the program!!!")
    break
  print(user)

  print("\n")

# Sem usar a palavra-chave "break", esta é outra implementação do mesmo programa de cima usando uma variável.
end = False
while end == False:
  user = input("Enter something to be repeated: ")
  if user=="end":
    print("Program Ended!!!")
    end = True
  else:
    print(user)

print("\n")

count = 1
# Implementação do loop WHILE
while count + 1 <= 20:
  if count % 5 == 0:
    print("SKIP")
    count += 1
    continue
  print(count)
  count += 1

print("\n")
# Implementação do loop FOR 
for i in range (1, 20):
  if i % 5 == 0:
    print("SKIP")
    continue
  print(i)


