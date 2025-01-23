import random
smwols = ["♥", "♦", "♣", "♠"]
numbers = ["6","7","8","9","10","J","Q","K","A"]

class Player:
    def __init__(self, name, points=0):
        self.Name=name

class Card:
    def __init__(self, type, simble):
        self.Type=type
        self.Simble=simble
    def SonwCards(self):
        print(f"""_____
|{self.Type}  |
| {self.Simble} |
|  {self.Type}|
-----""")

def GetCard():
    card1 = random.choice(coloda)
    coloda.remove(card1)
    return card1

coloda = []
players = []
Hand1 = []

def play():
    Hand1.append(GetCard())
    Hand1.append(GetCard())
    print(Hand1[0].Type,Hand1[1].Type)

for i in smwols:
    for j in numbers:
        card = Card(i,j)
        coloda.append(card)
for i in coloda:
    i.SonwCards()
for i in range(2):
    neme = input("напиши свое имя")
    players.append(Player(neme,))
    play()