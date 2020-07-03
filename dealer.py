class Dealer:
    def __init__(self, cards):
        self.type = 'dealer'
        self.cards = cards
        self.hand = []
        self.points = 0

    def current_hand(self, hand):
        self.hand = hand

    def hit(self, cards):
        self.hand.append(cards.draw_card('top'))

    def set_points(self, points):
        self.points = points

    def reset_deck(self, hands):
        for hand in hands:
            for card in hand:
                self.cards.return_card(card, 'bottom')
        for card in self.hand:
            self.cards.return_card(card, 'bottom')
