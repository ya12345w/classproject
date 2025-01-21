import random
import time

class Magic:
    def __init__(self,magicName,magicPower,magicType,magicBodyType, magicTime):
        self.MagicName=magicName
        self.MagicPower=magicPower
        self.MagicType=magicType
        self.MagicName=magicName
        self.MagicBodyType=magicBodyType
        self.MagicTime=magicTime

    def magic_action(self,h1,h2):

        if self.MagicType == 1:
            for i in self.MagicBodyType:
                if i == 1:
                    h2.Health -= self.MagicPower
                elif i == 2:
                    h2.Damage -= self.MagicPower
                    if h2.Damage <= -1:
                        h2.Damage = 0
                elif i == 3:
                    h2.Speed -= self.MagicPower
                    if h2.Speed <= -1:
                        h2.Speed = 0
                elif i == 4:
                    h2.Magic -= self.MagicPower
                    if h2.Magic <= -1:
                        h2.Magic = 0
                print()

        elif self.MagicBodyType == 2:
            for i in self.MagicBodyType:
                if i == 1:
                    h1.Health += self.MagicPower
                elif i == 2:
                    h1.Damage += self.MagicPower
                elif i == 3:
                    h1.Speed += self.MagicPower
                elif i == 4:
                    h1.Magic += self.MagicPower


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

        if rNumber <= self.Speed:
            return True
        else:
            return False
    def dealth(self):
        return self.Health <= 0
    def magicUse(self):
        rNumber = random.randint(1,100)
        return self.Magic >= rNumber


heroes = [
    Heroes("test", 300, 0, 0, 0, [0]),
    Heroes("Orc",150,25,10,0,[0]),
    Heroes("people",100,30,20,10,[4]),
    Heroes("mage",60,20,20,50,[2, 3])
         ]

Magics = [
    Magic("None", 0, 0, [0], 0),
    Magic("heal",40,2,[1], 0),
    Magic("fire ball",40,1,[1], 0),
    Magic("frozen ball",20,1,[2,3], 2),
    Magic("Strength up",10,2,[1,2,3], 3)
         ]

def Punch(h1, h2):

    if h2.evade():
        print(f"{h2.Race} уклонился от атаки")
    else:
        if h1.magicUse():
            randMagic = Magics[random.choice(h1.HeroMagicType)]
            randMagic.magic_action(h1, h2)
            print(f"{h1.Race} использовал магию {randMagic.MagicName}")
        else:
            h2.Health = h2.Health - h1.Damage
            print(f"{h1.Race} ударил {h2.Race}")

    if h2.dealth():
        print(f"{h1.Race} победил!")
        return True
    h2.Show_health()
a = 1
for i in heroes:
    print(f"{a}.{i.Race}")
    a += 1
Hero1, Hero2 = map(int,input("укажи номер двух героев церез пробел:").split())

while True:
    b = input("следующий ход")

    print(" ")
    p1= Punch(heroes[Hero1-1], heroes[Hero2-1])
    if p1:
        break
    print(" ")
    p2 = Punch(heroes[Hero2-1], heroes[Hero1-1])
    if p2:
        break