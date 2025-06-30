class Student: 
    #init default method ivvakapoina untundhi but parameters  pass cheyyaali ante ala cheyyaali
    def __init__(self,name,roll): #self is a reference variable in any method if we want to access var we use this
        self.name = name
        self.roll = roll
    def display(self): #ikkada seld 
        print(f"Name: {self.name}, Roll: {self.roll}")
s1 = Student("Swathi",57) #creating an object for a particular class
#print(s1) --> error: <__main__.Student object at 0x00000243FB351490>
print(s1.name)
s1.display()