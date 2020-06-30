import deck

deck_of_cards = deck.Deck()

# deck_of_cards.shuffle_deck('riffle')
# deck_of_cards.shuffle_deck('cut')
# deck_of_cards.shuffle_deck()

deck_of_cards.shuffle_deck('riffle')
for x in deck_of_cards.show_deck():
    print(x)
print(len(deck_of_cards.show_deck()
))