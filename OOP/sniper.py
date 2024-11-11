class Sniper:
    health = 100

    def __init__(self, name):
        self.name = name
    
    def shoot(self, sniper2):
        sniper2.health -= 20
        print(f'Атаковал {self}')
        print(f'У {sniper2} осталось {sniper2.health} единиц здоровья')

    def __str__(self) -> str:
        #* Когда принтим объект
        return self.name
    
sniper1 = Sniper('nikita')
sniper2 = Sniper('tima')

import random
while sniper1.health and sniper2.health:
    choice = random.randint(1,2)
    if choice == 1:
        sniper1.shoot(sniper2)
    else:
        sniper2.shoot(sniper1)

if sniper1.health:
    print(f'Победил {sniper1}')
else:
    print(f'Победил {sniper2}')
    

