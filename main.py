import random 

class Card():
    def __init__(self):

        # Creates random card upon instatiation
        
        card_values ={"Ace": 11,
                      "2": 2,
                      "3": 3,
                      "4": 4,
                      "5": 5,
                      "6": 6,
                      "7": 7,
                      "8": 8,
                      "9": 9,
                      "10": 10,
                      "Jack": 10,
                      "King": 10,
                      "Queen": 10}
        
        suit_values = ["Diamonds", "Hearts", "Spades", "Clubs"]
     
        self.card = random.choice(list(card_values))
        self.value = card_values[self.card]
        self.suit = random.choice(suit_values)


class player():
    def __init__(self):
        self.hand = []
def main():
    players = []
    spentCards = []
    
    while True:
        try:
            numPlayers = int(input("Enter the number of players: ")
            break
        except ValueError:
            print("Invalid number of players\n")
                     
    for i in range(0, numPlayers):
        players.append(Player())
    for i in players:
        while True:
            drawnCard = Card()
            if drawnCard in spentCards:
                pass
            else:
                break
        i.hand.append(drawnCard)
