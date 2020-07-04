# Class object for each player
class Player:
    def __init__(self, name, balance):
        """Initialize name and total balance of player"""
        self.type = 'player'
        self.name = name
        self.balance = balance
        self.hand = []
        self.points = 0

    def current_hand(self, hand):
        """Get hand for current round"""
        self.hand = hand

    def hit(self, cards):
        """Get an extra card in the hand"""
        self.hand.append(cards.draw_card('top'))

    def set_points(self, points):
        """Set the total points of current hand to each player"""
        self.points = points

    def change_balance(self, bet, result):
        """Change total balance according to the result"""
        if result == 'win':
            self.balance += bet
        else:
            self.balance -= bet
