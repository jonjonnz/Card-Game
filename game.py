import deck
from os import name, system
from time import sleep


# import pygame


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


deck_of_cards = deck.Deck()
deck_of_cards.shuffle_deck()
deck_of_cards.shuffle_deck('riffle')
deck_of_cards.shuffle_deck('cut')

game_on = True
print('--------------------BlackJack----------------------')


# name = input('Enter Name : ')
# coins = int(input('Enter your Starting value : '))
def get_total(hand):
    value = 0
    for card in hand:
        if card.value > 9:
            value += 10
        elif card.value == 1:
            if value < 11:
                value += 11
            else:
                value += 1
        else:
            value += card.value
    return value


def current_turn(turn, hand):
    score = get_total(hand)
    if turn == 'player':
        if score < 22:
            choice = input('What do you want to do ? 1.Hit 2.Stand :')
            if choice == '1':
                clear()
                hand.append(deck_of_cards.draw_card('top'))
                print('You got : ', end='')
                sleep(1)
                for card in hand:
                    print('[{}] '.format(card.show_card()), end='')
                print('\n')
                return current_turn('player', hand)

            elif choice == '2':
                return ['stand', score]
            else:
                print('Select Correct input')
                return current_turn(turn, hand)
        else:
            return ['busted', score]
    elif turn == 'dealer':
        if score < 17:
            hand.append(deck_of_cards.draw_card('top'))
            sleep(1)
            print('Dealer got : ', end='')
            for card in hand:
                print('[{}] '.format(card.show_card()), end='')
            print('\n')
            return current_turn(turn,hand)
        elif score > 21:
            return ['busted', score]
        else:
            return ['stand', score]


dealer = []
player = []
sequence = [player, dealer, player, dealer]
busted = None
while game_on:
    clear()
    for seq in sequence:
        seq.append(deck_of_cards.draw_card('top'))
    bet = int(input('Enter bet : '))
    print('Dealer got : [{}] [?]'.format(dealer[0].show_card()))
    sleep(1)
    print('You got : [{}] [{}]'.format(player[0].show_card(), player[1].show_card()))
    player_busted, player_score = current_turn('player', player)
    if player_busted != 'busted':
        print('Dealer got : [{}] [{}]'.format(dealer[0].show_card(),dealer[1].show_card()))
        dealer_busted, dealer_score = current_turn('dealer',dealer)

    game_on = False

# # Predefined Values


# width = 800
# height = 600
# FPS = 60
# # Initialize
# pygame.init()
# screen = pygame.display.set_mode(size=(width, height))  # Make a window
# pygame.display.set_caption("BlackJack")  # Set the window name
# clock = pygame.time.Clock()
# deck_of_cards = deck.Deck()
# running = True
# while running:
#     clock.tick(FPS)
#     # Inputs/Events
#     for event in pygame.event.get():
#         # Checking for closing the game
#         if event.type == pygame.QUIT:
#             running = False
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 card = deck_of_cards.draw_card('top')
#
#                 screen.blit(card.image, (0, 0))
#     pygame.display.update()
# pygame.quit()
