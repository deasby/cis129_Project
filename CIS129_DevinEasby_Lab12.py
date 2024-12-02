# Devin Easby
# CIS 129
# Module 12 Lab 

# Define the class 
class Pet:
    def __init__(self,name='',pet_type='', age=0): 
        self.name = name
        self.pet_type = pet_type
        self.age = age

    # Mutators
    def setName(self, name):
        self.name = name
    
    def setType(self,pet_type): 
        self.pet_type = pet_type 

    def setAge(self,age):
        self.age = age
    
    # Accessors 
    def getName(self): 
        return self.name
    
    def getType(self): 
        return self.pet_type
    
    def getAge(self):
        return self.age

# Main 
def main(): 
    animal = Pet()

    # Get values from user
    inputName = input("Enter a pet's name: ")
    animal.setName(inputName)

    inputType = input("Enter a pet's type: ")
    animal.setType(inputType)

    inputAge = int(input("Enter a pet's age: "))
    animal.setAge(inputAge)
  
    # Display user input 
    print(f"The pet name is {animal.getName()}")
    print(f"The pet type is {animal.getType()}")
    print(f"The pet age is {animal.getAge()}")

# Call the Main
if __name__ == '__main__':
    main()
