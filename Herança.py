class ClownFish(object):
    pass

nemo = ClownFish()
print(type(nemo))
print(isinstance(nemo, ClownFish))
print("\n") 

class Animal(object):
    pass

class Vertebrate(Animal):
    pass

class Fish(Vertebrate):
    pass

class ClownFish(Fish):
    pass

class TangFish(Fish):
    pass

nemo = ClownFish()

print(isinstance(nemo, ClownFish))
print(isinstance(nemo, TangFish))
print(isinstance(nemo, Animal))
print(isinstance(nemo, object))

class Fish(Animal):
    def speak(self): 
        return "Blub"

class ClownFish(Fish):
    pass

class TangFish(Fish):
    pass

nemo = ClownFish()
dory = TangFish()
print(nemo.speak())
print(dory.speak())

class TangFish(Fish):
    def speak(self):
        return "Hello, I'm a TangFish instance."
    
dory = TangFish()
print(dory.speak())

class ClownFish(Fish):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return "A ClownFish named "+self.name
    
nemo = ClownFish('Nemo')

print(nemo)

class Fish(Vertebrate):

    # self.name não é definido na classe Fish, mas é definido na classe ClownFish.
    def __str__(self):
        return "Hello, my name is {}".format(self.name)
    
class ClownFish(Fish): 
    def __init__(self, name):
        self.name = name

nemo = ClownFish("nemo")
print(nemo) 

class Fish(Vertebrate):
    def __init__(self, name):
        self.name = name

    # self.name não é definido na classe Fish, mas é definido na classe ClownFish.
    def __str__(self):
        return "Hello, my name is {}".format(self.name)
    
class ClownFish(Fish):
    def __init__(self, name):
        self.name = name

nemo = ClownFish("Nemo")

# __str__() está acessando o self.name a partir do nível filha
print(nemo)

nemo = Fish("clown_fish")

#  __str__ está acessando o atributo self.name da classe Fish
print(nemo)