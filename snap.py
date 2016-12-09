import random
from threading import Timer
import time 




class Card(object):
    # Hearts, Diamonds,Clubs,Spades
    suit_names = ['H', 'D', 'C', 'S']
    # Possible card ranks
    rank_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


    def __init__(self, suit, rank):
        self.suit = Card.suit_names[suit]
        self.rank = Card.rank_names[rank]
    def __str__(self):
        return self.suit + self.rank

    def grab_suit(self):
        return self.suit

    def grab_rank(self):
        return self.rank

    def draw(self):
        print self.suit + self.rank



class Deck:
    def __init__(self):
        #Create a deck in order
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)

    def shuffle(self):
        #Shuffle the cards
        random.shuffle(self.cards)

    def pop_card(self, i=1):
#i: index of the card to pop; by default, pops the first card.
        return self.cards.pop()

    def add_one_card(self, card):
        self.cards.append(card)

    def add_pile(self,cards):
        self.cards.extend(cards)

    def __len__(self):
        return len(self.cards)

    def __nonzero__(self):
        return bool(self.cards)

    def calc_value(self,card1,card2):
        return card1.rank != card2.rank

class Hand(object):

    def __init__(self, name = ''):
        self.cards = []
        self.value = 0
        self.name = name

    def add_one_card(self, card):
        self.cards.append(card)

    def add_pile(self,cards):
        self.cards.extend(cards)

    def __len__(self):
        return len(self.cards)

    def print_num_of_cards(self):
        return ' %s cards' %len(self.cards)

    def draw(self):
        return self.cards.pop()





def player_input():
    "Read user input, lower case it just to be safe"
    plin = raw_input().lower()
    if plin == 'h':
        display_players_hand()
    elif plin == 'd':
        deal_cards()
    elif plin == 'q':
        quit_game()
    else:
        print "Invalid Input...Enter h, s, d, or q: "
        player_input()

def quit_game():
    print 'Thanks for playing!'
    exit()

def intro():
    statement = '''Welcome to Snap! Match two cards and press SNAP!Press
 d to deal,h to show your card,ENTER to call 'Snap' and q to quit the game.'''
    print statement
    player_input()

def deal_cards():
    while deck:
        player.add_one_card(deck.pop_card())
        computer.add_one_card(deck.pop_card())
    else:
        print "The player has" + player.print_num_of_cards()
        print "The computer has" + computer.print_num_of_cards()
        print "Let's play!Press h to open a card on the table: "
        player_input()

def display_players_hand():
    deck.cards.append(computer.draw())
    print "Computer's Hand is: ", deck.cards[-1]
    deck.cards.append(player.draw())
    print "Player's Hand is: ", deck.cards[-1]
    #compare the two hands
    snap = ''
    tmr = Timer(1.0, computer_wins)
    if deck.calc_value(deck.cards[-1], deck.cards[-2]):
        print "There are %s cards on the table" %len(deck.cards)
        game_step()
    else:
        tmr.start()
        if snap == raw_input():
            tmr.cancel()
            player_wins()


def computer_wins():
    computer.add_pile(deck.cards)
    deck.cards[:] = []
    #print len(deck.cards)
    print "The computer says 'SNAP'!"
    print "The computer has" + computer.print_num_of_cards()
    print "The player has" + player.print_num_of_cards()
    game_step()

def player_wins():
    print"SNAP!"
    player.add_pile(deck.cards)
    deck.cards[:] = []
    print len(deck.cards)
    print "The player has" + player.print_num_of_cards()
    print "The computer has" + computer.print_num_of_cards()
    game_step()


def game_step():

    while len(player.cards) > 0 and len(computer.cards) > 0:
        print 'Press h to open another card: '
        player_input()
    else:
        print "Game over!"
        print "The player has" + player.print_num_of_cards()
        print "The computer has" + computer.print_num_of_cards()
        quit_game()


deck = Deck()
computer = Hand()
player = Hand()

deck.shuffle()  
intro()
