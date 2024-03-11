import collections
# namedtuple for class with attributes only. The first parameter is typename, the second parameter is filed_names
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    # initialize the ranks and suits
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # 13 types
    suits = 'spades diamonds clubs hearts'.split() # 4 types

    # initialize the _cards
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # overload the inside method __len__
    def __len__(self):
        return len(self._cards)

    # overload the inside method __getitem__
    def __getitem__(self, position):
        return self._cards[position]


# check for namedtuple: it overloads __repr__
deck = Card('7', 'diamonds')
print(deck)

# check for the overloaded __len__
deck = FrenchDeck()
print(len(deck))

# check for the overloaded __getitem__
print(deck[0])
print(deck[-1])

# use the inside random.choice to choose a card randomly
from random import choice
print(choice(deck))
print(choice(deck))

# because of the overloaded __getitem__ we can slice or lterate
print(deck[:3])
print('-------------')
for card in deck:
    print(card)
print('-------------')
# `for card in reversed(deck)` is also okay

# no overloaded __contains__, so the operator `in` run in a loop
print(Card('Q', 'hearts') in deck)
print(Card('7', 'beasts') in deck)

# how to sort
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(ccard):
    rank_value = FrenchDeck.ranks.index(ccard.rank)
    return rank_value * len(suit_values) + suit_values[ccard.suit]


print('----------')
for card in sorted(deck, key=spades_high):
    print(card)
print('----------')