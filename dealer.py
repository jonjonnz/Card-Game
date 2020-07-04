# Class object for dealer
class Dealer:
    def __init__(self):
        """Initialize dealer and hand and points """
        self.type = 'dealer'
        self.hand = []
        self.points = 0

    # def current_hand(self, hand):
    #     """Set hand of current round"""
    #     self.hand = hand

    def hit(self, cards):
        self.hand.append(cards.draw_card('top'))

    def set_points(self, points):
        """Set points of current round"""
        self.points = points

    def reset_deck(self, hands):
        """Return all the cards from current hand back to the deck"""
        for hand in hands:
            for card in hand:
                self.cards.return_card(card, 'bottom')
        for card in self.hand:
            self.cards.return_card(card, 'bottom')

    def deal_cards(self, cards, players):
        """Deal cards to each player"""
        hands = []
        for i in range(len(players)):
            hands.append(cards.draw_card('top'))
        self.hit(cards)
        for i in range(len(players)):
            hands.append(cards.draw_card('top'))
        self.hit(cards)
        for i in range(len(players)):
            players[i].current_hand([hands[i], hands[i + len(players)]])
