import random

deck_suits = { 'Spades': '♠', 'Hearts': '♥','Clubs': '♣', 'Diamonds': '♦'}
deck_ranks = {
    1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'
}


class Deck:

    def __init__(self):
        self.card_list = []
        self.build_deck()

    def build_deck(self):
        for suit, symbol in deck_suits.items():
            for value, rank in deck_ranks.items():
                self.card_list.append(Card(rank, suit, value, symbol))

    def show_deck(self):
        for card in self.card_list:
            print(card.show_card())

    def draw_card(self):
        return self.card_list.pop(random.randrange(52))


class Card:
    def __init__(self, name, suit, value, symbol):
        self.name = name
        self.suit = suit
        self.value = value
        self.symbol = symbol
        self.card = self.name + self.symbol

    def show_card(self):
        return self.card


deck_of_cards = Deck()
deck_of_cards.show_deck()
