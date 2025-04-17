# Class definition
class Pet:
    # Creating attributes
    def __init__(self, name):
        self.name = name
        self.hunger = 6
        self.energy = 7
        self.happiness = 8
        self.tricks = []

    # Creating a method for the object to eat
    def eat(self):
        self.hunger = max(self.hunger - 3, 0)
        self.happiness = min(self.happiness + 1, 10)
        if self.hunger > 5:
            print(self.name + " has eaten.")
        else:
            print(self.name + " is hungry.")

    # Creating a method for the object to sleep
    def sleep(self):
        self.energy = min(self.energy + 5, 10)
        print(self.name + " is sleeping.")

    # Creating a method for the object to play
    def play(self):
        if self.energy >= 2:
            self.energy -= 2
            self.happiness = min(self.happiness + 2, 10)
            self.hunger = min(self.hunger + 1, 10)
            print(self.name + " is playing!")
        else:
            print(self.name + " is too tired to play.")

    # Method to check the status of the object
    def get_status(self):
        print(self.name + "'s Status")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")

    # Method to train an object
    def train(self, trick):
        if trick not in self.tricks:
            self.tricks.append(trick)
            self.happiness = min(self.happiness + 1, 10)
            print(f"{self.name} learned a new trick: {trick}!")
        else:
            print(f"{self.name} already knows how to {trick}.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")


