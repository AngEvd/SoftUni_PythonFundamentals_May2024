cards = input().split(" ")
shuffles = int(input())

middle = len(cards) // 2

while shuffles > 0:
    top_deck = cards[:middle]
    bottom_deck = cards[middle:]
    shuffled_deck = []

    for top, bottom in zip(top_deck, bottom_deck):
        shuffled_deck.append(top)
        shuffled_deck.append(bottom)

    cards = shuffled_deck
    shuffles -= 1

print(cards)
