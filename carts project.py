import random
simbols = ["♠", "♣", "♦", "♥"]
numbers = ["6","7","8","9","10","J","Q","K","A"]

class Player:
    def __init__(self, name, points=0,cards=None):
        self.Name=name
        self.Points=points
        self.Cards=cards
    def pointsCount(self):
        self.Points += 1

class Card:
    def __init__(self, simble, type):
        self.Type=type
        self.Simble=simble
    def ShowCards(self):
        print(f"""_____
|{self.Simble}  |
| {self.Type} |
|  {self.Simble}|
-----""")

def GetCard():
    card1 = random.choice(coloda)
    return card1

coloda = []
players = []
playerN1 = 0
playerN2 = 0

def play():
    player1 = GetCard()
    player2 = GetCard()
    player1.ShowCards()
    player2.ShowCards()

    if numbers.index(player1.Type) > numbers.index(player2.Type):
        players[0].pointsCount()
        print(f"{players[0].Name} Wins {players[0].Points}")
    elif numbers.index(player1.Type) < numbers.index(player2.Type):
        players[1].pointsCount()
        print(f"{players[1].Name} Wins {players[1].Points}")
    else:
        if simbols.index(player1.Simble) > simbols.index(player2.Simble):
            players[0].pointsCount()
            print(f"{players[0].Name} Wins {players[0].Points}")
        elif simbols.index(player1.Simble) < simbols.index(player2.Simble):
            players[1].pointsCount()
            print(f"{players[1].Name} Wins {players[1].Points}")
        else:
            print("tie")

for i in simbols:
    for j in numbers:
        card = Card(i,j)
        coloda.append(card)
players = [
    Player(input("напиши свое имя")),
    Player(input("напиши свое имя"))
]

while True:
    play()
    a=input()
    if players[0].Points >= 10:
        print(f"{players[0].Name} Win!")
    elif players[1].Points >= 10:
        print(f"{players[0].Name} Win!")
    else:
        print("error")



