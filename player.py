class Player:
    def __init__(self, name, balance):
        self.type = 'player'
        self.name = name
        self.balance = balance
        self.hand = []
        self.points = 0

    def current_hand(self, hand):
        self.hand = hand

    def hit(self, cards):
        self.hand.append(cards.draw_card('top'))

    def set_points(self, points):
        self.points = points

    def change_balance(self, bet, result):
        if result == 'win':
            self.balance += bet
        else:
            self.balance -= bet
