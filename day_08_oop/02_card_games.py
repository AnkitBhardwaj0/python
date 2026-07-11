import random
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "J", "Q", "K"]
        self.cards = []

        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        if len(self.cards) == 0:
            print("No cards left!")
            return None
        
        return self.cards.pop()

    def __str__(self):
        return f"No of cards remaining in deck - {len(self.cards)}"


deck1= Deck()
card = deck1.deal()

print(card)
print(deck1)