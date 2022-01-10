"""
package game_classes

"""
from src.game_classes.PlayerAbstract import PlayerAbstract


class PlayerHuman(PlayerAbstract):

    def __init__(self, name):
        super().__init__(name)
        import Data
        self.data = Data.instance()

    def move(self):
        #TODO tu musi sie pokazac ekran do wprowadzania literek, z którego potrzebuje pobrać
        #TODO (x_start,y_start), (x_end,y_end) i słowo
        #TODO po wciśnięciu koniec tury pobieram rzeczy i sprawdzam czy słowo jest w słowniku jak nie, to jeszcze raz daję zrobić ruch
        #TODO przy wprowadzaniu trzeba zastrzec gdzie mozna wprowadzać literki -> żeby tworzyły słowo w linii
        #TODO x_start, y_start, x_end, y_end, word = COS
        #TODO return x_start, y_start, x_end, y_end, word
        #TODO W klasie game literki dodadzą się do planszy i zostaną nam przyznane punkty
        pass
