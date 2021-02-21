import GameParts as gp
import os
def clear(): 
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

loses = 0
wins = 0
ties = 0

def Game():   
    clear()
    global wins 
    global loses
    global ties
    #Game variables
    gameState = 1
    deck = gp.Deck()
    player1 = gp.Hand(0)
    dealer = gp.Hand(1)

    #Before starting the game shuffle the cards
    deck.suffleCards()

    #Game starts with 2 cards each and one dealer card unknown 
    for deal in range(2):
        player1.hit(deck)
        dealer.hit(deck)    
    #Shows initial hands
    print('Dealer Hand is:\n# #\n{}\n'.format(dealer.cards[-1].showCard()))
    print('Player hand:')
    print(player1.showCards())
    print('Player hand Value: {}\n'.format(player1.handValue))
    #Lets the player decide if hit or stay
    while(gameState):
        choice = input('Select an option 0: Stay | 1:Hit\n')
        clear()   
        if(choice == '1'):
            player1.hit(deck)
            print('Player hits: {}\n Player hand: '.format(player1.cards[-1].showCard()))
            print(player1.showCards())
            print('Player hand value:{}\n'.format(player1.handValue))
            if(player1.handValue>21):#Check if player did not bust
                gameState = 0            
        else:#If stay the dealer hits until more than 17 
            while(dealer.handValue < 17):
                dealer.hit(deck)
                print('Dealer hits: {}\n Dealer hand: '.format(dealer.cards[-1].showCard()))
                print(dealer.showCards())
                print('Dealer hand value is: {}\n'.format(dealer.handValue))
            gameState = 0
            print('Dealer hand:')
            print(dealer.showCards())
            print('Dealer hand value is: {}\n'.format(dealer.handValue))
        
    #Game result is calculated
    if(player1.handValue>21):
        print("You busted with {} you lose".format(player1.handValue))
        loses += 1
    elif(player1.handValue == 21 and dealer.handValue == 21):
        print("Both players have 21, its a tied game")
        ties += 1
    elif(dealer.handValue>21 and player1.handValue<=21):
        print("Dealer busted with {} you win".format(dealer.handValue))
        wins += 1
    elif(dealer.handValue <= 21 and player1.handValue < dealer.handValue):
        print("Dealer score({}) is higher than yours({}) you lose".format(dealer.handValue,player1.handValue))
        loses += 1
    elif(dealer.handValue <= 21 and player1.handValue == dealer.handValue):
        print("Dealer score({}) is same as yours({}), you lose".format(dealer.handValue,player1.handValue))
        loses += 1
    elif(dealer.handValue < 21 and player1.handValue>= dealer.handValue):
        print("Your score({}) is higher than dealers({}) you win".format(player1.handValue,dealer.handValue))
        wins += 1

game = 1

while(game):
    Game()
    print('-----------Score----------------\nWins:{}\nLoses:{}\nTies:{}\n'.format(wins,loses,ties))
    game = int(input("Want to play again??? 0:No 1:Yes \n"))
    clear()


    



