import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """A class representing a standard French deck of cards."""
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def __init__(self):
        """Initialize a new deck of cards."""
        self.cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        """Return the number of cards in the deck."""
        return len(self.cards)

    def __getitem__(self, position):
        """Return the card at the given position."""
        return self.cards[position]

    def __repr__(self):
        """Return a string representation of the deck."""
        cards = ', '.join(str(card) for card in self.cards)
        return f"FrenchDeck({cards})"

    def __iter__(self):
        """Return an iterator over the cards in the deck."""
        return iter(self.cards)

    def __reversed__(self):
        """Return a reverse iterator over the cards in the deck."""
        return reversed(self.cards)

    def draw_card(self):
        """Draw a random card from the deck."""
        return random.choice(self.cards)

    def spades_high(self, card):
        """Return a value for ranking a card, with spades being the highest suit."""
        rank_value = self.ranks.index(card.rank)
        return rank_value * len(self.suit_values) + self.suit_values[card.suit]


if __name__ == "__main__":
    deck = FrenchDeck()
    print(deck)

    print(f"Random card: {deck.draw_card()}")

    # Support slicing
    print(deck[:3])
    print(deck[11:13])

    # The deck is iterable and reversible
    for card in deck:  # iterate over the deck
        print(card)

    for card in reversed(deck):  # iterate in reverse
        print(card)

    # Check if a card is in the deck
    print(Card('K', 'hearts') in deck)
    print(Card('7', 'diamonds') in deck)

    # Sorting
    for card in sorted(deck, key=deck.spades_high):
        print(card)
