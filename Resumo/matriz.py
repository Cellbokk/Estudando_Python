import numpy as np

u = np.ones((3,3,3))
print(u)

print(u.shape)
print(np.ones((2,3)))
print(np.ones((3, 2)))

# Importar diferentes pacotes usados para análise de dados
# ... "as opt" significa que o programador poderia usar a abreviatura de "opt" para se referir a esta biblioteca, em vez de digitar o nome completo
import scipy.optimize as opt
import numpy as np
import matplotlib.pyplot as plt


# Dados brutos inseridos manualmente pelo usuário
I =[4.0, 3.5, 3.0, 2.5, 2.0]
B =[1.31, 1.14, 0.97 ,0.81, 0.76]
IError = [0.2, 0.2, 0.2, 0.2, 0.2]
BError = [0.03, 0.02, 0.04, 0.02, 0.05]

print("estimated B for each error \n")
for i in range (5) :
  print(str(I[i]) + "+-" + str(IError[i]) + ": " + str(B[i]) + "+-" + str(BError[i]))
  
# Aplicar a biblioteca Numpy para formatar a lista de dados brutos em uma matriz multidimensional
 # Isto é necessário para a otimização das funções e para o uso adequado do pacote Scipy
xdata = np.array(I)
ydata = np.array(B)
xerror = np.array(IError)
yerror= np.array(BError)

# Definir função linear para ajuste
def func(h, m, b):
    return m*h + b


# w dá o parâmetro estimado para m e b, armazenado na matriz quadrada de w e u
# A informação que falta _ retornar sobre variância e covariância

# w é uma matriz com informações sobre o valor da inclinação e do y-intercepção
w, u = opt.curve_fit(func, xdata, ydata) 

# Aplicar coordenadas x e resultado otimizado sobre o ajuste da curva para encontrar a "Linha do Melhor Ajuste".
yfit = func(xdata,*w)
    
# Use o pacote Matplotlib para fazer gráficos de dados
  # 1. Gráfico das barras de erro para cada valor x 
  # 2. Gráfico da "Linha do Melhor Ajuste"

# Nota: há opções para personalizar o visual de seu gráfico com diferentes parâmetros
plt.errorbar(I, B, xerr=IError, yerr = BError, fmt='o', ms = 3)
plt.plot(xdata,yfit,label="Fit", linewidth=1.5, linestyle='dashed')

# Adicionar título e etiquetas ao gráfico
plt.title('I vs. B of the Electromagnet')
plt.xlabel('Electromagnet Current I (A)')
plt.ylabel('Magnetic Field B (T)')


print("\n Estimated parameters of m and b: ", w)
print("\n Estimated variance of m & b: ", np.sqrt(np.diag(u)))

# Se necessário, é assim que você poderia salvar o gráfico em sua máquina local.  
# Mas aqui NÃO precisamos salvar o gráfico, por isso comentaremos esta linha. 

# Especifique o nome da imagem como o parâmetro
### plt.savefig('IvsB.jpg')

# Nota: se você estiver mostrando e armazenando o gráfico, certifique-se de SALVAR antes de PROJETAR.
plt.show()