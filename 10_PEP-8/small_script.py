"""
Iterator 
"""

class MyIterator:
     def __init__(self):
         print("init 40") 
         self.i = 40 
     # 
     def __iter__(self): 
        print("On a appelé __iter__")
        return self 
     # 
     def __next__(self): 
        print("On a appelé __next__")
        self.i += 2 
        if self.i > 56 : 
           raise StopIteration()
        return self.i 

for i in MyIterator(): 
      print(i)

print(list(MyIterator()))
print(sum(MyIterator()))
  



"""
Generator yield
"""

def my_generator():
    i = 40
    while i <= 56:
        i += 2
        yield i   # generator ! 


for i in my_generator():
    print(i)


# Autre exemple 
def generator(beginning, end):  
    print("    On commence !")

    cpt = beginning
    while cpt <= end:
        if cpt % 2 == 0:
            print("    On s'arrete au yield")
            yield float(cpt)
            print("    On reprend après le yield")
        else:
            print("    On s'arrete au yield")
            yield str(cpt)
            print("    On reprend après le yield")
        cpt += 1
    yield "C'est bientôt la fin"
    yield "C'est VRAIMENT bientôt la fin"
    yield "Là c'est la fin"

for i in generator(4, 8):
    print(i)

