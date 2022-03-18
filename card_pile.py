# should this be part of card.py, or the game manager object?
# basically just a LIFO stack (would calling it stack cause less or more confusion?)
import card
import random
from operator import attrgetter


class Pile:
    # able to generate a new deck, shuffle, sort, draw, receive a new card, display contents, get count
    # can represent main deck, player hands, discard piles, play area
    cards = []

    def __init__(self, new_deck=False):
        if new_deck:
            self.generate()
            # TODO: should we auto-shuffle a fresh deck?

    def generate(self):
        # have options for generate 52 with 0-4 jokers, pinochle deck...
        for suit in card.Suit:
            if suit != card.Suit.NONE:
                # TODO: beware off-by-one here!
                rank = 0
                while rank < 13:  # magic number, need to use a max_rank here
                    rank += 1
                    self.cards.append(card.Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def sort(self, rank_first=True):
        # sort by rank or suit
        # there is room for improvement here, could probably be more streamlined and robust
        if rank_first:
            self.cards.sort(key=attrgetter('rank', 'suit'))
        else:
            # self.cards = sorted(self.cards, key=attrgetter('suit', 'rank'))
            self.cards.sort(key=attrgetter('suit', 'rank'))  # same thing?

            # Using those functions, the above examples become simpler and faster:
            #
            # >> > from operator import itemgetter, attrgetter
            #
            # >> > sorted(student_tuples, key=itemgetter(2))
            # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
            #
            # >> > sorted(student_objects, key=attrgetter('age'))
            # [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
            #
            # The operator module functions allow multiple levels of sorting.For example, to sort by grade then by age:
            #
            # >> > sorted(student_tuples, key=itemgetter(1, 2))
            # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
            #
            # >> > sorted(student_objects, key=attrgetter('grade', 'age'))
            # [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
            #

    def draw(self, specific_card=-1):
        # default to top card of pile, allow specific card for playing cards from hand
        # basically just pop the stack and return drawn card
        # might get confusing, player drawing a card should pull from main deck,
        # but currently planning to play from hand by using draw.
        # try not to overthink it, but this might need to be thought about more.
        if specific_card == -1:
            return self.cards.pop()  # not fond of multiple  returns, might need a temp variable and return once.
        else:
            return self.cards.pop(specific_card)
        # sample usage: hand.receive(main_deck.draw())

    def receive(self, new_card):
        # receive, take, accept, insert? what is the least confusing name?
        # is this just redundant and not really needed?
        self.cards.append(new_card)

    def display(self):
        # TODO: when using graphics, need to implement style
        #  need to print 20ish to a line? might need to have card display variables and not rely on their own print
        # stacked, staggered, space, alignment vert/horz/none
        for c in range(len(self.cards)):
            self.cards[c].display()

    def get_count(self):
        return len(self.cards)

