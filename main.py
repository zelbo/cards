# deck of cards basic manipulation for learning purposes
# use a que?
# piles: hand, discard, play, main
# shuffle
# deal(hand)
# card class: back.png, value(rank?), suit, color?, is_face_up bool, is_tapped bool
# game controller has list of piles (main, discard, hand)
# pile styles: stacked, staggered, spaced, alignment(vert/horz/none)
# TODO: draw and discard need to be streamlined and straightforward - pile.take(from_pile), pile.give(to_pile)
#  these methods should not refer to each other. maybe use pile.send(card), pile.receive(card) as underlying?
# some things to do for various games:
#  player play zones, common play zone, pass to left or right, draw, discard...
#  some of it can be implemented per game, but should have a common vocabulary for standard actions

import card_pile

main_deck = card_pile.Pile(True)
main_deck.shuffle()
discard = card_pile.Pile()
player_one_hand = card_pile.Pile()
play_area = card_pile.Pile()


def display_all():
    global main_deck
    global discard
    global player_one_hand
    global play_area
    print('Main Deck size: ', main_deck.get_count())
    main_deck.display()
    # TODO: player one draw 5 cards, discard 1, play 1
    #  sort hand
    #  display all piles


display_all()
