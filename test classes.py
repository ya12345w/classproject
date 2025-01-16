import random
import time

class Magic:
    def __init__(self,magicName,magicPower,magicType,magicBodyType):
        self.MagicName=magicName
        self.MagicPower=magicPower
        self.MagicType=magicType
        self.MagicName=magicName
        self.MagicBodyType=magicBodyType



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