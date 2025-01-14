import random
import time

# class Car:
#     name = "lexus"
#     speed = 30
#     color = "black"
#
#     def info(self):
#         return self.color
#
# car1 = Car()
# car2 = Car()
# car2.color="white"
# print(car2.info())
# print(car1.info())

# class Cat:
#     name="barsik"
#     color="white"
#     weikht=10

# class SuperCar:
#     def __init__(self,name,speed,color):
#         self.Name=name
#         self.Speed=speed
#         self.Color=color
#
# car3 = SuperCar("tesla",100,"gray")
# car4 = SuperCar("lada",90,"blue")
#
# print(car3.Name)
# maleName = ["Alexander", "Alexander", "Alexander", "Alexander", "Alexander", "Michael", "Michael", "Michael", "Michael",
#             "William", "William", "William", "James", "James", "name"]
# femaleName = ["Anna", "Anna", "Anna", "Anna", "Anna", "Elizabeth", "Elizabeth", "Elizabeth", "Elizabeth", "Elizabeth",
#               "Victoria", "Victoria", "Victoria", "Sophia", "Sophia", "name"]
#
# Gender = random.choice(["Male", "Female"])
# HairColor = random.choice(["blue", "red", "brown", "black", "green", "yellow", "orange"])
# Old = random.randint(1, 80)
# if Gender == "Male":
#
# class Person:
#     def __init__(self,name,age,fml,contacts,national):
#         self.Name=name
#         self.Age=age
#         self.FML=fml
#         self.Contacts=contacts
#         self.National=national
#     def __repr__(self):
#         return self.Name
# people = []
#
# while True:
#     name,age,fml,contacts,national = map(str,input("введи свое имя возраст пол контакты и национальность через пробел:").split())
#     person = Person(name,age,fml,contacts,national)
#
#     people.append(person)
#
#     print(*people)
class Magic:
    def __init__(self,magicName,magicPower,magicType,magicBodyType):
        self.MagicName=magicName
        self.MagicPower=magicPower
        self.MagicType=magicType
        self.MagicName=magicName



class Heroes:
    def __init__(self,race,health,damage,speed,magic):
        self.Race=race
        self.Health=health
        self.Damage=damage
        self.Speed=speed
        self.Magic=magic

    def Show_health(self):
        print(f"у {self.Race} осталось здоровья: {self.Health} ")

    def evade(self):
        rNumber = random.randint(1,100)
        print(rNumber)

        if rNumber <= self.Speed:
            return True
        else:
            return False
    def dealth(self):
        if self.Health <= 0:
            return True


heroes = [
    Heroes("Orc",200,25,10,0),
    Heroes("people",100,30,20,10),
    Heroes("mage",60,20,20,50)
         ]


def Punch(h1, h2):
    if h2.evade():
        print(f"{h2.Race} уклонился от атаки")
    else:
        h2.Health = h2.Health - h1.Damage
        print(f"ударил {h1.Race}")

    if h2.dealth():
        print(f"{h1.Race} победил!")
        return True
    h2.Show_health()


while True:
    time.sleep(3)

    print(" ")
    p1= Punch(heroes[0], heroes[1])
    if p1:
        break
    print(" ")
    p2 = Punch(heroes[1], heroes[0])
    if p2:
        break