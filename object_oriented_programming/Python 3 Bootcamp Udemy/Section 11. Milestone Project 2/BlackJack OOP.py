'''
BlackJack OOP
Alan Preciado
03-04-19
'''
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    
    def __init__(self, suit='Hearts', rank='Two'):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '{0} of {1}'.format(self.suit, self.rank) # return a string
    
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                card = Card(suit,rank)
                self.deck.append(card) # instantitate 52 unique card objects
    
    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__() #Using the str method from the other class
        return deck_composition

    def shuffle(self):
        random.shuffle(self.deck) # shuffle card objects in deck
        
    def deal(self): # deal out means take out a card from the deck
        single_card = self.deck.pop() #remove last element from the list
        return single_card
    
    
class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank] # we want to know the added value of the cards in hand
        if card.rank == 'Ace':
            self.aces += 1
            
    def adjust_for_ace(self): # if we pass 21 we adjust the attribute vale
        while self.value > 21 and self.aces: # self.aces: Any non-zero numeric value is considered true.
            self.value -= 10
            self.aces -= 1
  

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self): # add bet to total
        self.total += self.bet
    
    def lose_bet(self): # substract bet from total
        self.total -= self.bet            
 

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('Enter the chips you want to bet: ')) # you want to modify the object's attribute
        except ValueError:
            print('Modify your input, the ammount of chips must be an integer!')
        else:
            if chips.bet > chips.total:
                print('You do not have enough chips to bet that amount, your total is: ', chips.total)
            else:
                break            
    
    
def hit(deck,hand):
    # Withdraw card and add value of it to hand
    dealed_card = deck.deal() 
    hand.add_card(dealed_card) # other format: hand.add_card(deck.deal()) 
    
    # Verify if have to correct for ace
    hand.adjust_for_ace()      

    
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Hit or Stand?, enter h or s")
        
        if x[0].lower() == 'h':
            print('Player hits')
            hit(deck,hand)
        
        elif x[0].lower() == 's':
            print('Player stands')
            playing = False
        
        else:
            print('Unclear input, try again')
            continue
            
        break            
                        
def show_some(player,dealer):
    # 1. game starts
    # 2. each time player takes card
    # 3. dealer's first card is hidden and all of player's cards are visible
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1]) 
    print("\nPlayer's Hand:", *player.cards, sep='\n ') # asterisk * symbol is used to print every item in a collection
    
def show_all(player,dealer):
    # show all cards and values
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)            
                      
def player_busts(player, dealer, chips):
    print('Player busts') # busts means going over 21 (hence loosing the round)
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print('Player wins')
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print('Dealer busts')
    chips.lose_bet()
    
def dealer_wins(player, dealer, chips):
    print('Dealer wins')
    chips.win_bet()
    
def push(player, dealer):
    print('Player and dealer tie, this is a push')
    
            
while True:
    # Print an opening statement
    #print('This is BlackJack, get as close as 21 in order to win\n\ 
    #Dealer can only hit until she/he reaches 17, ace is either 1 or 11')

    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck and deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal()) # Withdraw card from deck
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
        
    # Set up the Player's chips
    player_chips = Chips() # 100 chips by default
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
    
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)
 
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
            
        # Show all cards
        show_all(player_hand, dealer_hand)
    
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
            
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        
        else: 
            push(player_hand, dealer_hand)
    
    # Inform Player of their chips total 
    print("\nPlayer's total chips is: ", player_chips.total)
    
    # Ask to play again
    play_again = input("Would you like to play again? y or n ")
    
    if play_again[0].lower() == 'y':
        playing = True
        continue
    else:
        print("That's it for today...")
        break                          