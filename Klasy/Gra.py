import Plansza
import time

class Gra:
    def __init__(self):
        self.czas_rozpoczecia = 0
        self.aktualny_wynik = 0
        self.plansza = Plansza()


    def rozpocznij(self):
        self.czas_rozpoczecia = time.time()


    def zatrzymaj(self):
        print('!!! POKAŻ JAKIEŚ OKIENKO I ZATRZYMAJ GRE !!!')

    def wznow(self):
        print('!!! UKRYJ OKIENKO I KONTYNUUJ GRE !!!')

    def zakoncz(self):
        print('!!! DODAJ DO STATYSTYK I WYJDZ DO MAIN MENU !!!')
        czas_gry = time.time()-self.czas_rozpoczecia
        sec = czas_gry%60
        czas_gry = czas_gry//60
        min = czas_gry%60
        godz = czas_gry//60
        print('Czas gry to {}H {}M {}S'.format(godz, min, sec))
        