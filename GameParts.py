import random as r

class Deck():
    cardsValues = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    cardsSuits = ['♠','♥','♦','♣']
    cards = None
    def __init__(self):#Create deck with suits and values
        self.cards = []
        for cardSuit in self.cardsSuits:
            for cardValue in self.cardsValues:
                self.cards.append(Card(cardValue, cardSuit))

    def suffleCards(self):
        r.shuffle(self.cards)
    def takeCard(self):
        return self.cards.pop(0)


class Card():
    value = None
    suit = None
    def __init__(self, cardValue, cardSuit):
        self.value = cardValue
        self.suit = cardSuit

    def showCard(self):
        return self.suit + ' ' + self.value


class Hand():
    isDealer = None
    cards = []
    acesCount = None
    handValue = None
    def __init__(self,isDealer):
        self.isDealer = isDealer
        self.cards = []
        self.acesCount = 0
        self.handValue = 0

    def hit(self,deck):#Get a card from the top of the deck and adds it to the hand value
        self.cards.append(deck.takeCard())
        card = self.cards[-1]
        if(card.value.isnumeric()):
            self.handValue += int(card.value)
        elif(card.value == "A"):
            if(not self.isDealer):
                self.acesCount += 1
            elif((self.handValue+11) <= 21):
                self.handValue += 11
            else:
                self.handValue += 1
        else:
            self.handValue += 10
        if(self.acesCount > 0 and not self.isDealer):#Automaticly sets the Ace value if the sum is less than 21
            for ace in range(self.acesCount):                
                if((self.handValue+11)<=21):
                    self.handValue+=11
                else:
                    self.handValue+=1
        self.acesCount = 0

    def showCards(self):
        cardsString = ''
        for card in self.cards:
            cardsString += '\n'+card.showCard()
        return cardsString

        
    
        

