import random
import pygame
import os
# Defaults for a deck
suits = {'Spades': '♠', 'Hearts': '♥', 'Clubs': '♣', 'Diamonds': '♦'}
ranks = {1: 'A', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'J', 12: 'Q', 13: 'K'}


# Images
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "deck_imgs")


# Make a full deck of cards
class Deck:

    def __init__(self):
        self.deck = []
        self.build_deck()

    def build_deck(self):
        """Use the defaults to make a full deck of 52 cards"""
        for suit, symbol in suits.items():
            for value, rank in ranks.items():
                self.deck.append(Card(rank, suit, value, symbol))

    def show_deck(self):
        """Print the value of each card in the deck onto the terminal"""
        if __name__ == '__main__':
            for card in self.deck:
                print(card.show_card())
        else:
            return [x.show_card() for x in self.deck]

    def draw_card(self, position):
        """Draw a card from a specified position in the deck"""
        if position == 'top':
            return self.deck.pop(0)
        elif position == 'bottom':
            return self.deck[len(self.deck) - 1]
        elif position == 'random':
            return self.deck.pop(random.randrange(0, len(self.deck)))

    def return_card(self, card, position):
        """Return a card to a specific position in the deck"""
        if position == 'top':
            self.deck = self.deck[::-1]
            self.deck.append(card)
            self.deck = self.deck[::-1]
        elif position == 'bottom':
            self.deck.append(card)
        elif position == 'random':
            n = random.randrange(0, len(self.deck))
            self.deck = (self.deck[:-n] + [card, ] + self.deck[-n:])

    def shuffle_deck(self, shuffle_type=None):
        """Shuffle the deck using riffle shuffle or a cut shuffle or a random shuffle"""
        if shuffle_type == 'riffle':
            temp_deck = []
            self.deck = self.deck[::-1]
            deck_count = int(len(self.deck) / 2)
            for i in range(deck_count):
                temp_deck.append(self.deck[i])
                temp_deck.append(self.deck[i + int(len(self.deck) / 2)])
            if deck_count % 2 != 0:
                temp_deck.append(self.deck[len(self.deck) - 1])
            self.deck = temp_deck[::-1]
        elif shuffle_type == 'cut':
            n = random.randrange(0, len(self.deck))
            self.deck = (self.deck[-n:] + self.deck[:-n])

        else:
            for i in range(len(self.deck)):
                r = random.randrange(0, len(self.deck))
                self.deck[i], self.deck[r] = self.deck[r], self.deck[i]


# Make a card using ranks, values ,suits ,and symbols
class Card:
    def __init__(self, name, suit, value, symbol):
        self.name = name
        self.suit = suit
        self.color = 'Red' if self.suit in ['Hearts', 'Diamonds'] else 'Black'
        self.value = value
        self.symbol = symbol
        self.card = self.name + self.symbol
        self.image = pygame.image.load(os.path.join(img_folder,self.suit[0]+str(value) + '.png'))
    def show_card(self):
        """Show the current drawn card"""
        return self.card
