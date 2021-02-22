import random as r

class Deck():
    cardsValues = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    cardsSuits = ['♠','♥','♦','♣']
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
    
    def __init__(self, cardValue, cardSuit):
        self.value = cardValue
        self.suit = cardSuit

    def showCard(self):
        return self.suit + ' ' + self.value


class Hand():
    def __init__(self,isDealer):
        self.isDealer = isDealer        
        self.cards = []
        self.handValue = 0

    def hit(self,deck):#Get a card from the top of the deck and adds it to the hand value
        self.cards.append(deck.takeCard())      
        self.handValue = 0  
        acesCount = 0
        for card in self.cards:
            if(card.value.isnumeric()):
                self.handValue += int(card.value)
            elif(card.value == "A"):
                acesCount+=1          
            else:
                self.handValue += 10
        for i in range(0, acesCount):
            if((self.handValue + 11) > 21):
                self.handValue += 1
            else:
                self.handValue += 11


    def showCards(self):
        cardsString = ''
        for card in self.cards:
            cardsString += '\n'+card.showCard()
        return cardsString

        
    
        

