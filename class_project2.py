# One person is going to be the bartender and the other the costumer. It's happening either in 
# Mr.Copão in Copacabana or in Boteco Belmonte in Ipanema - this will be chosen randomly 

import random 

# Choosing the place for the interaction
def initial_conditions():
    bar = ['Mr.Copao', 'Boteco_Belmonte'] # In case you want to use a method 
    bar_choice = random.choice(bar)
    waiting_time = ('5', '10', '15') # minutes 
    waiting_time = random.choice(waiting_time)
    drinks = {'Negroni': 30, 'Caipirinha': 25, 'Vodka': 20}
    return bar, bar_choice, waiting_time, drinks

bar, bar_choice, waiting_time, drinks = initial_conditions() # unpacked 

    
# Creating the costumer 
class Costumer:
    def __init__(self, name, gender, money): # Ideia: use the gender to randomly choose a name
        self.name = name
        self.gender = gender
        self.order = input(f'Qual é o seu pedido, as opções são: {drinks.keys()}')
        self.money = money
        self.drink = []
    
    def transactions_1(self):
        self.money -= drinks.values()
        self.drink = self.drink.append(self.order) 
        pass

    


# Creating the bartender 
class Bartender:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.waiting_time = waiting_time # Set the time in a conditional for each drink
    
    def taking_the_order(self, Costumer):
        self.taking_order = Costumer.order


# SIMULATING: so far working just fine 
costumer_1 = Costumer('Rodrigo', 'Male', 'Negroni')
bartender_1 = Bartender('Camerero', 'Male')

print(f'''Hi, my name is {bartender_1.name} and thank you for being in {bar_choice}! 
Your order is {costumer_1.order} and the waiting time is {waiting_time}''')