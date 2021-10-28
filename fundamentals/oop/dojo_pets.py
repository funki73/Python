class Pet:

    def _init_(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 200
        self.energy = 50
        self.noise = ruff

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f'Time to eat')
        return self

    def play(self):
        self.health += 5
        print(f'Go get the ball')
        return self

    def noise(self):
        print(f'RUFF RUFF')
        return self

class Ninja:
    def _init_(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self
        
    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.noise()
        return self

peppy = Pet('Peppy', 'Pug', 'Fetch')

ninja1 = Ninja('Jo', 'Mama', 'dog', 'greenie', 'kibble')

print(ninja1.walk)
print(ninja1.feed)
print(ninja1.bathe)

