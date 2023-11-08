class Player:

    def __init__(self, name, numberOfChips, currentMoney, isTurn, cards):
        self.name = name
        self.numberOfChips = numberOfChips
        self.currentMoney = currentMoney
        self.isTurn = isTurn
        self.cards = cards

    def __str__(self):
        return f"{self.name} has ${self.currentMoney} on the table."

    def __repr__(self):
        return f"Player(\'{self.name}\', ${self.currentMoney})"

    def shouldBet(self):
        return NotImplementedError

    def placeBet(self):
        return NotImplementedError
