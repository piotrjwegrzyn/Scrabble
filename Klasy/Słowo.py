class Ranking:
    slowo = ''
    suma_punktow = 0

    def __init__(self, slowo):
        self.slowo = slowo

    def policz_punkty(self):
        for char in self.slowo:
            