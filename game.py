import random


class ADGame:
    def __init__(self, chipCost, buyInAmount):
        self.chipCost = chipCost
        self.buyInAmount = buyInAmount
        self.deck = [x for x in range(2, 12)
                     for _ in range(4)]  # Index 0 = top of deck

    def shuffle(self):
        random.shuffle(self.deck)

    def dealCard(self):
        card = self.deck.pop(0)
        return card

    def initialDeal(self):
        cardOne = self.dealCard()
        cardTwo = self.dealCard()
        return [cardOne, cardTwo]
