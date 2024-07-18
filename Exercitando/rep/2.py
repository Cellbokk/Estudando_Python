import os 
print("Seja bemvindo, porfavor coloque seu nome e sua senha para o cadastro!\n")
nome = str(input("Digite seu nome:")).strip()
senha = int(input("Digite sua senha:"))
os.system("clear")

print("dados Salvos!!")
print("Porfavor agora verifique o cadastro:\n")

while True:
    try:
        nomed = str(input("Digite seu nome:")).strip()
        senhad = int(input("Digite sua senha:"))
        if nome == nomed and senha == senhad:
            print(f"Ola {str(nome)} seja bem vindo")
            break
        else:
            os.system("clear")
            print("Senha ou nome errado tente novamente!!")

    except ValueError:
        print("ta errado")

