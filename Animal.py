class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal): #access the parent class ka properties to this child class
    def bark(self):
        print("Dog barks bow bow")
d = Dog()
d.speak()
d.bark()
