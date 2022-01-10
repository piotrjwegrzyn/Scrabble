"""
package game_classes

"""
from src.game_classes.PlayerAbstract import PlayerAbstract


class PlayerHuman(PlayerAbstract):

    def __init__(self, name):
        super().__init__(name)
        from src.game_classes.Data import Data
        self.data = Data.instance()

    def move(self):
        #TODO tu musi sie pokazac ekran do wprowadzania literek, z którego potrzebuje pobrać
        #TODO (x_start,y_start), (x_end,y_end) i słowo
        #TODO po wciśnięciu koniec tury pobieram rzeczy i sprawdzam czy słowo jest w słowniku jak nie, to jeszcze raz daję zrobić ruch
        #TODO przy wprowadzaniu trzeba zastrzec gdzie mozna wprowadzać literki -> żeby tworzyły słowo w linii
        #TODO x_start, y_start, x_end, y_end, word = COS
        #TODO return x_start, y_start, x_end, y_end, word
        #TODO W klasie game literki dodadzą się do planszy i zostaną nam przyznane punkty
        self.check_if_well_placed()

    def check_if_well_placed(self):
        x = []
        y = []
        for ele in letters_placed:
            x.append(ele[1])
            y.append(ele[2])
        x.sort()
        y.sort()

        is_vertical_or_horizontal = 'vertical'
        for i in range(1, len(x)):
            if x[i] != x[i-1]:
                is_vertical_or_horizontal = 'horizontal'
        if is_vertical_or_horizontal == 'horizontal':
            for i in range(1, len(y)):
                if y[i] != y[i-1]:
                    is_vertical_or_horizontal = 'bad'

        if is_vertical_or_horizontal == 'bad':
            return False
        elif is_vertical_or_horizontal == 'vertical':
            for i in range(min(y), max(y)):
                if i not in y and self.data.board_pools[x[0]][i] == '':
                    return False
            return True

        elif is_vertical_or_horizontal == 'horizontal':
            for i in range(min(x), max(x)):
                if i not in x and self.data.board_pools[i][y[0]] == '':
                    return False
            return True
