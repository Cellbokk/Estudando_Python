class Livraria:

    pass

livro = Livraria()
print(livro)

type(livro)
print(type(livro))

# Outra maneira de verificar o tipo de algum objeto
print(isinstance(livro, Livraria))

class LibraryBook (object):   

    def __init__(self, title, author, pub_year, call_no):
          self.title = title
          self.author = author
          self.year = pub_year
          self.call_number = call_no
          self.checked_out = False


    livro.title = "Harry Potter and the Philosopher's Stone"
    livro.author = ('Rowling', 'J.K.')
    livro.year = 1998
    livro.call_number = "PZ7.R79835"

    print(livro.author)