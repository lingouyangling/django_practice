# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle
from time import sleep

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

SUITE_NAMES = dict(zip(SUITE, ['Hearts', 'Diamonds', 'Spades', 'Clubs']))

class Deck():
    """I'm a docstring!"""
    def __init__(self):
        print('Generating new deck...')
        sleep(1)
        self.all_cards = [(i,j) for i in SUITE for j in RANKS]

    def shuffle(self):
        print('Shuffling cards...')
        sleep(1)
        shuffle(self.all_cards)

    def split_in_half(self):
        print('Splitting deck...')
        sleep(1)
        return (self.all_cards[:26], self.all_cards[26:])

class Player():

    def __init__(self, name, cards=[]):
        self.name = name
        self.cards = cards

    def turn_up_one(self):
        return self.cards.pop()

    def remove_three(self):
        three = []
        for _ in range(3):
            three.append(self.cards.pop())
        return three

    def add_cards_to_bottom(self, cards):
        shuffle(cards)
        self.cards = cards + self.cards

    def still_have_cards(self):
        return len(self.cards) != 0

    def less_than_three_cards(self):
        return len(self.cards) < 3


######################
#### GAME PLAY #######
######################
# greetings
print("Welcome, let's begin...")
sleep(1)
# get player names
p1_name = input("Player 1! What's your name?")
sleep(1)
p2_name = input("Player 2! What's your name?")
sleep(1)
# initialize deck
deck = Deck()
deck.shuffle()
half1, half2 = deck.split_in_half()

# assign cards to palyers
p1 = Player(p1_name, half1)
p2 = Player(p2_name, half2)

# start game
rounds = 0
wars = 0
table_cards = []

# check cards
while p1.still_have_cards() and p2.still_have_cards():
    rounds += 1
    print("#" * 40)
    print(f"Round: {rounds}!")
    print("#" * 40)
    sleep(1)
    print(f"{p1.name} has {len(p1.cards)} cards")
    print(f"{p2.name} has {len(p2.cards)} cards")
    sleep(1)
    # turn up one card
    print("Both players turning up one card...")
    sleep(1)
    p1_card = p1.turn_up_one()
    p2_card = p2.turn_up_one()
    # cards are face up
    print(f"{p1.name}: {SUITE_NAMES[p1_card[0]]} {p1_card[1]}")
    print(f"{p2.name}: {SUITE_NAMES[p2_card[0]]} {p2_card[1]}")
    sleep(1)
    # add to table
    table_cards.append(p1_card)
    table_cards.append(p2_card)
    # compare
    if RANKS.index(p1_card[1]) > RANKS.index(p2_card[1]):
        print(f"{p1.name} has higher card, adding all cards to {p1.name}...")
        sleep(1)
        p1.add_cards_to_bottom(table_cards)
        table_cards = []
    elif RANKS.index(p1_card[1]) < RANKS.index(p2_card[1]):
        print(f"{p2.name} has higher card, adding all cards to {p2.name}...")
        sleep(1)
        p2.add_cards_to_bottom(table_cards)
        table_cards = []
    else:
        # start war
        print("Both cards have the same rank, trying to start a War...")
        sleep(1)
        if p1.less_than_three_cards() and p2.less_than_three_cards():
            print("Both players have less than 3 cards now. Failed to start the war!")
            sleep(1)
        elif p1.less_than_three_cards():
            print(f"{p1.name} has less than 3 cards now. Failed to start the war!")
            sleep(1)
        elif p2.less_than_three_cards():
            print(f"{p2.name} has less than 3 cards now. Failed to start the war!")
            sleep(1)
        else:
            # turn up three cards
            wars += 1
            print("Starting the War...")
            sleep(1)
            print("Both players removing three cards to the table and waiting for a new round...")
            sleep(1)
            table_cards.extend(p1.remove_three())
            table_cards.extend(p2.remove_three())

# over game
winner = (p1.still_have_cards() and p1.name) or (p2.still_have_cards() and p2.name)
print("#" * 100)
print("GAME OVER!")
print(f"Total Rounds: {rounds}")
print(f"Total Wars: {wars}")
print("#" * (len(f"{winner} is the WINNER!")+4))
print("# "+f"{winner} is the WINNER!" + " #")
print("#" * (len(f"{winner} is the WINNER!")+4))
