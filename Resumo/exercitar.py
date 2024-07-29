num1 = float(input("Primeiro número:"))
num2 = float(input("Segundo número:"))
num3 = float(input("Terceiro número:"))

if num1 < num2:
    a = num1
    num1 = num2
    num2 = a

if num1 < num3:
    b = num1
    num1 = num3
    num3 = b

if num2 < num3:
    c = num2
    num2 = num3
    num3 = c

print(f"1° = {num1}")
print(f"2° = {num2}")
print(f"3° = {num3}")



