dict = {'a' : 5, 'b' : 50, 'c' : 100}

print(dict['b'])

dict['b'] = 200

print(dict['b'])

# Os valores no dicionário podem ser misturados
# Vejamos um exemplo com dict{}, um dicionário vazio iniciado acima.
# Primeiro, vamos inserir alguns pares de chaves/valores no programa. 

dict["greeting"] = "hello message"
dict["alphabet"] = ['a', 'b', 'c', 'd', 'e']
dict["check-in"] = False
dict["phoneNumber"] = 8007782346

dict
# Nota IMPORTANTE: a chave deve ser um objeto imutável (algo que não pode ser modificado)
# A string é imutável, porque você não poderia simplesmente apagar um caractere em uma string. Uma string é uma string, do jeito que ela é.

# Vemos acima que uma lista pode ser um valor no dicionário. 
# O que acontece quando tentamos fazer dela uma chave?

# ERROR: tipo inalcançável de lista 

# Porque poderíamos modificar a lista inserindo novos elementos, ordenando elementos, apagando elementos ou outras formas de modificá-la, mas ela NÃO PODE ser uma chave


dict[['a','b', 'c']] = [False, True, False]
# Mas como a tupla é imutável, podemos substituir a lista por uma tupla
dict[('a','b', 'c')] = [False, True, False]

dict
# Podemos também buscar todas as chaves
dict.keys()
# Ou todos os valores
dict.values()
# Os elementos de um dicionário também podem retornar como um par.
dict.items()