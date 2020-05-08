


"""
def decorator(func): 
    def inner(): 
        # do something
        return func()
    return inner
"""

def e_t(func): 
    def inner():
        print("Maison... Téléphone... Maison...")  
        return func()
    return inner

@e_t
def gertie(): 
    print('Je lui ai appris à parler ! Ecoute !')


gertie()	



@decorator
def karadoc():
    print("Le gras, c'est la vie.")






class CoffeeMachine(): 
    #
    water_level = 100 
    # 
    def _start_machine(self): 
    # Start the machine 
        if self.water_level > 20: 
            return True 
        else : 
            print("Please add water!")
            return False 
    #
    def __boil_water(self): 
        return "boiling..."
    def make_coffee(self): 
        # Make a new coffee!
        if self._start_machine(): 
            self.water_level -= 20 
            print(self.__boil_water())
            print("Coffee is ready")


machine = CoffeeMachine()

for i in range(0,5): 
    machine.make_coffee()

print("Make Coffee: Public",machine.make_coffee())
print("Start machine: Protected",machine._start_machine())
print("Boil Water: Private", machine._CoffeeMachine__boil_water())





























