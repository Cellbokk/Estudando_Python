list2 = ['hello', 'hola', 'ola']

print("o Primeiro elemento da lista e", list2[0])

list3 = ["john", "male", 20, False]

# Remover um elemento da lista especificando o elemento que você deseja remover
list2.remove('hello')
# list2 após o 'hello' é REMOVIDA
list2

# Inserir um novo elemento como um local específico, no index 1
list2.insert(1,'hallo')
list2[1]

# Anexar um novo elemento no FIM da lista
list2.append('bye')
list2

#Outra maneira de remover um elemento: pop()
#pop() permite que você identifique uma posição 


list2.append("hello")

list2.pop()

list2

#As listas também podem ser ordenadas.O método de ordenação depende de como a interface comparável é implementada para os objetos da lista. Neste caso da list2, sort() funciona ordenando caracteres individuais na string de acordo com o código ASCII.

list2.sort()
list2

# Imprimir itens na lista como string, separados por uma vírgula
",".join(list2)

# Você também pode ter uma lista de listas. Por exemplo:

lists = []
lists.append([1,2,3])
lists.append(['a','b','c'])

lists
# Da mesma forma, você pode indexar as listas multidimensionais.

lists[1]
#['a', 'b', 'c']
lists[1][0]
#'a'

# Como len() retorna int, para concatená-la a uma string, precisamos computá-la.
print("size of list1 = " + str(len(list1)))
print("size of list2 = " + str(len(list2)))