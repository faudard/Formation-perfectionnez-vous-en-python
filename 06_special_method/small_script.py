
class Hack: 
    def __len__(self): 
        print('Wow, I just hacked Python!')
        return 5 

a = Hack()

print(len(a))

class Babar: 
    def __repr__(self): 
        return "Je suis un éléphant très spécial !"

a = Babar()
print(a)
