import random
import time

class Magic:
    def __init__(self,magicName,magicPower,magicType,magicBodyType):
        self.MagicName=magicName
        self.MagicPower=magicPower
        self.MagicType=magicType
        self.MagicName=magicName
        self.MagicBodyType=magicBodyType

    def magic_action(self,h1,h2):
        h1Lst = [h1.Race,h1.Health,h1.Damage,h1.Speed]
        h2Lst = [h2.Race,h2.Health,h2.Damage,h2.Speed]
        if self.MagicType == 1:
            for i in self.MagicBodyType:
                h2Lst[i] -= self.MagicPower

        elif self.MagicBodyType == 2:
            for i in self.MagicBodyType:
                h1Lst[i] +=  self.MagicPower


class Heroes:
    def __init__(self,race,health,damage,speed,magic,heroMagicType):
        self.Race=race
        self.Health=health
        self.Damage=damage
        self.Speed=speed
        self.Magic=magic
        self.HeroMagicType=heroMagicType

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

    def magicUse(self):
        rNumber = random.randint(1,100)

        if self.Magic <= rNumber:
            #доделать шанс активации


heroes = [
    Heroes("Orc",200,25,10,0,None),
    Heroes("people",100,30,20,10,3),
    Heroes("mage",60,20,20,50,1)
         ]

Magics = [
    Magic("heal",40,2,[1]),
    Magic("fire ball",40,1,[1]),
    Magic("frozen ball",20,1,[2,3]),
    Magic("Strength up",10,2,[1,2,3])
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