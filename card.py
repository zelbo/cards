from enum import Enum


class Suit(Enum):
    # Alternating colors: diamonds (lowest), followed by clubs, hearts, and spades (highest).
    # color can be found by modulo (suit.value odd == black, even == red)
    NONE = 0
    SPADE = 1
    HEART = 2
    CLUB = 3
    DIAMOND = 4


class Color(Enum):
    NONE = 0
    RED = 1
    BLACK = 2


class Card:
    # are these initializations needed here if we are using __init__?
    # allow any rank, leave the deciphering of ace, king, queen, etc. to the individual game?
    # or include standard face card here while also exposing underlying values?
    # for jokers, allow rank 0 for two suits, remove the other two?
    rank = 0
    suit = Suit.NONE
    color = Color.NONE
    is_face_up = False
    is_tapped = False  # not needed for most standard card games, but might come in handy?

    def __init__(self, rank=0, suit=Suit.NONE):
        self.rank = rank
        self.suit = suit
        self.color = self.get_color()

    def flip(self):
        self.is_face_up = not self.is_face_up

    def tap(self):  # poorly named, also untaps
        # TODO: change to floop?
        self.is_tapped = not self.is_tapped

    def get_color(self):
        card_color = Color.NONE
        if self.suit.value % 2 == 0:  # abstract this to a utility function?
            card_color = Color.RED
        else:
            card_color = Color.BLACK
        return card_color

    def display(self):
        # TODO: A, J, Q, K
        # TODO: mess with colors? https://stackoverflow.com/questions/287871/how-to-print-colored-text-to-the-terminal
        display_suit = ''
        if self.suit == Suit.SPADE:
            display_suit = '\u2660'
        elif self.suit == Suit.CLUB:
            display_suit = '\u2663'
        elif self.suit == Suit.HEART:
            display_suit = '\u2665'
        else:
            display_suit = '\u2666'

        print(self.rank, display_suit)
