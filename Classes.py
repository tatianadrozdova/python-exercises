# Define a class with its function:


class Animals():
    animalData = []
    countAnimals = 0
    animalID = 1

    @staticmethod
    def printAnimalData():
        for animal in Animals.animalData:
            print("No.: %s, name: %s, group: %s, species: %s, breed: %s, age: %s, firColor: %s, " \
                  "eye color: %s, speak: %s, ID: %s"\
                  % (animal.animalCount(), animal.name, animal.group, animal.species, animal.breed, animal.age, animal.firColor,\
                     animal.eyeColor, animal.speak, animal.id))

    @classmethod
    def printAnimalByName(selfClass, name):

        for animal in selfClass.animalData:
            if animal.name.lower() == name.lower():
                print("Name: %s, group: %s, species: %s, breed: %s, age: %s, firColor: %s, eye color: %s, speak: %s, "\
                  "ID: %s, No.: %s"\
                  % (animal.name, animal.group, animal.species, animal.breed, animal.age, animal.firColor, animal.eyeColor, animal.speak, \
                     animal.id, animal.animalCount()))

    @classmethod
    def printAnimalBySpecies(selfClass, species):

        for animal in selfClass.animalData:
            if animal.species.lower() == species.lower():
                print("Species: %s, name: %s, group: %s, breed: %s, age: %s, firColor: %s, eye color: %s, "\
                      "speak: %s, ID: %s, No.: %s"\
                  % (animal.species, animal.name, animal.group, animal.breed, animal.age, animal.firColor, animal.eyeColor, \
                     animal.speak, animal.id, animal.animalCount()))

    @classmethod
    def printAnimalByBreed(selfClass, breed):

        for animal in selfClass.animalData:
            if animal.breed.lower() == breed.lower():
                print("Breed: %s, name: %s, group: %s, species: %s, age: %s, firColor: %s, eye color: %s, speak: %s, "\
                  "ID: %s, No.: %s"\
                  % (animal.breed, animal.name, animal.group, animal.species, animal.age, animal.firColor, animal.eyeColor, animal.speak, \
                     animal.id, animal.animalCount()))


    @classmethod
    def printAnimalBySound(selfClass, speak):

        for animal in selfClass.animalData:
            if animal.speak.lower() == speak.lower():
                print("Speak: %s, breed: %s, name: %s, group: %s, species: %s, age: %s, firColor: %s, eye color: %s, "\
                  "ID: %s, No.: %s"\
                  % (animal.speak, animal.breed, animal.name, animal.group, animal.species, animal.age, animal.firColor, animal.eyeColor,\
                     animal.id, animal.animalCount()))


    @classmethod
    def printAnimalByFirColor(selfClass, firColor):

        for animal in selfClass.animalData:        
            if animal.firColor.lower() == firColor.lower():
                print("FirColor: %s, breed: %s, name: %s, group: %s, species: %s, age: %s, eye color: %s, speak: %s, "\
                  "ID: %s, No.: %s" \
                  % (animal.firColor, animal.breed, animal.name, animal.group, animal.species, animal.age, animal.eyeColor, animal.speak, \
                     animal.id, animal.animalCount()))


    @classmethod
    def printAnimalByEyeColor(selfClass, eyeColor):

        for animal in selfClass.animalData:
            if animal.eyeColor.lower() == eyeColor.lower():
                print("Eye color: %s, name: %s, group: %s, species: %s, breed: %s, age: %s, firColor: %s, speak: %s, " \
                  "ID: %s, No.: %s"\
                  % (animal.eyeColor, animal.name, animal.group, animal.species, animal.breed, animal.age, animal.firColor, animal.speak, \
                     animal.id, animal.animalCount()))


    @classmethod
    def printAnimalByGroup(selfClass, group):

        for animal in selfClass.animalData:
            if animal.group.lower() == group.lower():
                print("Group: %s, breed: %s, name: %s, species: %s, age: %s, firColor: %s, eye color: %s, speak: %s, "\
                  "ID: %s, No.: %s"\
                  % (animal.group, animal.breed, animal.name, animal.species, animal.age, animal.firColor, animal.eyeColor, animal.speak,\
                     animal.id, animal.animalCount()))


    @staticmethod
    def removeAnimalByName(name):

        for animal in Animals.animalData:
            if animal.name == name:
                Animals.animalData.remove(animal)
                
        return Animals.animalData
        
    
    def __init__(self, name, group = None, species = None, breed = None, age = None, firColor = None, eyeColor = None, speak = None):
        self.name = name
        self.group = group
        self.species = species
        self.breed = breed
        self.age = age
        self.firColor = firColor
        self.eyeColor = eyeColor
        self.speak = speak
        self.id = Animals.animalID
        Animals.animalID += 1
        
    def animalCount(self):
        if self in self.animalData:
            return self.animalData.index(self) + 1

    
    def addAnimal(self):
        self.animalData.append(self)
        Animals.countAnimals += 1
        return self.animalData


    def removeAnimal(self):

        for animal in self.animalData:
            if animal == self:
                self.animalData.remove(animal)
                
        return self.animalData
        
    

class Feline(Animals):
    countFelines = 0

    @staticmethod
    def amountOfFelines():
        print("The total amount of cats is %s" % Feline.countFelines)

              
    def __init__(self, name, species = None, breed = None, age = None, firColor = None, eyeColor = None, speak = None,  group = "Feline"):
        super().__init__(name, species, breed, age, firColor, eyeColor, speak, group)
        Feline.countFelines += 1

   
class HouseCat(Feline):

    def __init__(self, name, breed = None, age = None, firColor = None, eyeColor = None, group = "Feline", species = "Housecat", speak = "Mew"):
        super().__init__(name, species, breed, age, firColor, eyeColor, speak,  group)
           

class Lion(Feline):

    def __init__(self, name, breed = None, age = None, firColor = None, eyeColor = None, group = "Feline", species = "Lion", speak = "Row"):
        super().__init__(name, species, breed, age, firColor, eyeColor, speak,  group)
        
        
class Tiger(Feline):

    def __init__(self, name, breed = None, age = None, firColor = None, eyeColor = None, group = "Feline", species = "Tiger", speak = "Row"):
        super().__init__(name, species, breed, age, firColor, eyeColor, speak,  group)
        


class Canine(Animals):
    countCanines = 0

    @staticmethod
    def amountOfCanines():
        print("The total amount of canine is %s" % Canine.countCanines)

              
    def __init__(self, name, species = None, breed = None, age = None, firColor = None, eyeColor = None, speak = None,  group = "Canine"):
        super().__init__(name, group, species, breed, age, firColor, eyeColor, speak)
        Canine.countCanines += 1

   
class Dog(Canine):

    def __init__(self, name, breed = None, age = None, firColor = None, eyeColor = None, group = "Canine", species = "Dog", speak = "Uf"):
        super().__init__(name, species, breed, age, firColor, eyeColor, speak,  group)
        
        
        
class Fox(Canine):

    def __init__(self, name, breed = None, age = None, firColor = None, eyeColor = None, group = "Canine", species = "Fox", speak = "af"):
        super().__init__(name, species, breed, age, firColor, eyeColor, speak,  group)
        
        
class Wolfe(Canine):

    def __init__(self, name, breed = None, age = None, firColor = None, eyeColor = None, group = "Canine", species = "Wolfe", speak = "Au"):
        super().__init__(name, species, breed, age, firColor, eyeColor, speak,  group)
        

Camino = HouseCat("Camino", "Simese", "3", "Black", "Yellow")
Sunny = HouseCat("Sunny", "Norwegian", "10", "Orange and White", "Green")
Tim = Lion("Tim","African", "12", "Orange", "Yellow")
Tigro = Tiger("Tigro", "Siberian", "15", "Orange and Black", "Yellow")
Jake = Dog("Jake", "Mix", "11", "Orange and white", "Brown")
Foxy = Fox("Foxy", "Arctic Fox", "10", "White", "Blue")
Wolfy = Wolfe("Wolfy", "Forest Wolf", "8", "Grey", "Brown")
Animals.addAnimal(Camino)
Animals.addAnimal(Sunny)
Animals.addAnimal(Tim)
Animals.addAnimal(Tigro)
Animals.addAnimal(Jake)
Animals.addAnimal(Foxy)
Animals.addAnimal(Wolfy)

Animals.printAnimalData()
# result
#No.: 1, name: Camino, group: Feline, species: Housecat, breed: Simese, age: 3, firColor: Black,eye color: Yellow, speak: Mew, ID: 1
#No.: 2, name: Sunny, group: Feline, species: Housecat, breed: Norwegian, age: 10, firColor: Orange and White,eye color: Green, speak: Mew, ID: 2
#No.: 3, name: Tim, group: Feline, species: Lion, breed: African, age: 12, firColor: Orange,eye color: Yellow, speak: Row, ID: 3
#No.: 4, name: Tigro, group: Feline, species: Tiger, breed: Siberian, age: 15, firColor: Orange and Black,eye color: Yellow, speak: Row, ID: 4
# No.: 5, name: Jake, group: Canine, species: Dog, breed: Mix, age: 11, firColor: Orange and white, eye color: Brown, speak: Uf, ID: 5
# No.: 6, name: Foxy, group: Canine, species: Fox, breed: Arctic Fox, age: 10, firColor: White, eye color: Blue, speak: af, ID: 6
# No.: 7, name: Wolfy, group: Canine, species: Wolfe, breed: Forest Wolf, age: 8, firColor: Grey, eye color: Brown, speak: Au, ID: 7
print(" ")

Animals.printAnimalByName("Camino")
Animals.printAnimalByName("Sunny")
Animals.printAnimalByName("Tim")
Animals.printAnimalByName("Tigro")
# result
# Name: Camino, group: Feline, species: Housecat, breed: Simese, age: 3, firColor: Black, eye color: Yellow, speak: Mew,ID: 1, No.: 1
# Name: Sunny, group: Feline, species: Housecat, breed: Norwegian, age: 10, firColor: Orange and White, eye color: Green, speak: Mew,ID: 2, No.: 2
# Name: Tim, group: Feline, species: Lion, breed: African, age: 12, firColor: Orange, eye color: Yellow, speak: Row,ID: 3, No.: 3
# Name: Tigro, group: Feline, species: Tiger, breed: Siberian, age: 15, firColor: Orange and Black, eye color: Yellow, speak: Row,ID: 4, No.: 4
print(" ")

Animals.printAnimalBySpecies("Housecat")
# result:
# Species: Housecat, name: Camino, group: Feline, breed: Simese, age: 3, firColor: Black, eye color: Yellow,speak: Mew, ID: 1, No.: 1
# Species: Housecat, name: Sunny, group: Feline, breed: Norwegian, age: 10, firColor: Orange and White, eye color: Green,speak: Mew, ID: 2, No.: 2
print(" ")

print(" ")
Animals.printAnimalByBreed("Norwegian")
# result
# Breed: Norwegian, name: Sunny, group: Feline, species: Housecat, age: 10, firColor: Orange and White, eye color: Green, speak: Mew,ID: 2, No.: 2
print(" ")

Animals.printAnimalBySound("Rowwww")
# result
# Speak: Row, breed: African, name: Tim, group: Feline, species: Lion, age: 12, firColor: Orange, eye color: YellowID: 3, No.: 3
# Speak: Row, breed: Siberian, name: Tigro, group: Feline, species: Tiger, age: 15, firColor: Orange and Black, eye color: YellowID: 4, No.: 4
print(" ")

Animals.printAnimalByFirColor("orange")
# result
# FirColor: Orange and White, breed: Norwegian, name: Sunny, group: Feline, species: Housecat, age: 10, eye color: Green, speak: MewID: 2, No.: 2
# FirColor: Orange, breed: African, name: Tim, group: Feline, species: Lion, age: 12, eye color: Yellow, speak: RowID: 3, No.: 3
# FirColor: Orange and Black, breed: Siberian, name: Tigro, group: Feline, species: Tiger, age: 15, eye color: Yellow, speak: RowID: 4, No.: 4
# FirColor: Orange and white, breed: Mix, name: Jake, group: Canine, species: Dog, age: 11, eye color: Brown, speak: Uf, ID: 5, No.: 5
print(" ")

Animals.printAnimalByEyeColor("green")
# result
# Eye color: green, name: Sunny, group: Feline, species: Housecat, breed: Norwegian, age: 10, firColor: Orange and White, speak: MewID: 2, No.: 2
print(" ")

Animals.printAnimalByGroup("canine")
print(" ")
Animals.printAnimalByGroup("feline")
print(" ")
Canine.amountOfCanines()
print(" ")

Feline.amountOfFelines()
# result
# The total amount of cats is 4
print(" ")


Animals.removeAnimal(Sunny)
Animals.removeAnimal(Jake)
Animals.printAnimalData()
# result
#No.: 1, name: Camino, group: Feline, species: Housecat, breed: Simese, age: 3, firColor: Black, eye color: Yellow, speak: Mew, ID: 1
#No.: 2, name: Tim, group: Feline, species: Lion, breed: African, age: 12, firColor: Orange, eye color: Yellow, speak: Row, ID: 3
#No.: 3, name: Tigro, group: Feline, species: Tiger, breed: Siberian, age: 15, firColor: Orange and Black, eye color: Yellow, speak: Row, ID: 4
#No.: 4, name: Foxy, group: Canine, species: Fox, breed: Arctic Fox, age: 10, firColor: White, eye color: Blue, speak: af, ID: 6#No.: 5, name: Wolfy, group: Canine, species: Wolfe, breed: Forest Wolf, age: 8, firColor: Grey, eye color: Brown, speak: Au, ID: 7
#No.: 5, name: Wolfy, group: Canine, species: Wolfe, breed: Forest Wolf, age: 8, firColor: Grey, eye color: Brown, speak: Au, ID: 7
print(" ")

Animals.removeAnimalByName("Tim")
Animals.removeAnimalByName("Foxy")
Animals.printAnimalData()
# result
#No.: 1, name: Camino, group: Feline, species: Housecat, breed: Simese, age: 3, firColor: Black, eye color: Yellow, speak: Mew, ID: 1
#No.: 2, name: Tigro, group: Feline, species: Tiger, breed: Siberian, age: 15, firColor: Orange and Black, eye color: Yellow, speak: Row, ID: 4
#No.: 3, name: Wolfy, group: Canine, species: Wolfe, breed: Forest Wolf, age: 8, firColor: Grey, eye color: Brown, speak: Au, ID: 7
print(" ")

