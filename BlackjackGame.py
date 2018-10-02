# Gra Blackjack - gracze (1-7) współzawodniczą z komputerem

import GryModule, KartyModule


class BJ_Karta(KartyModule.Karty):
    """Karta do gry BlackJack"""
    AS_wartosc = 1

    @property
    def wartosc(self):
        if self.front:
            wrt = BJ_Karta.RANGA.index(self.ranga) + 1
            if wrt > 10:
                wrt = 10
        else:
            wrt = None
        return wrt


class BJ_Talia(KartyModule.Talia):
    """Talia kart do gry BlackJack"""
    def zapelnij_talie(self):
        for kolor in BJ_Karta.KOLOR:
            for ranga in BJ_Karta.RANGA:
                self.karty.append(BJ_Karta(ranga, kolor))


class BJ_Reka(KartyModule.Reka):
    """Ręka gracza z kartami"""
    def __init__(self, imie_gracza):
        super(BJ_Reka, self).__init__()
        self.imie_gracza = imie_gracza

    def __str__(self):
        pokaz = self.imie_gracza + ": " + super(BJ_Reka, self).__str__()
        if self.total:
            pokaz += "(" + str(self.total) + ")"
        return pokaz

    @property
    def total(self):
        # Jeśli karta w ręce ma wartość None, to i wartość sumy wynosi None
        for karta in self.karty:
            if not karta.wartosc:
                return None

        # suma wartości kart - każdy AS traktowany jako 1
        t = 0
        for karta in self.karty:
            t += karta.wartosc

        # czy reka zawiera asa
        jest_as = False
        for karta in self.karty:
            if karta.wartosc == BJ_Karta.AS_wartosc:
                jest_as = True

        # jeśli ręka zawiera Asa, a suma jest odpowiednio niska, as traktowany jako 11
        if jest_as and t <= 11:
            # dodaj 10, bo już jest dodane 1 za asa
            t += 10

        return t

    def odpada(self):
        return self.total > 21


class BJ_Gracz(BJ_Reka):
    """Gracz w grze"""
    def dobiera(self):
        odpowiedz = GryModule.zapytaj_tak_nie(self.imie_gracza + ", dobierasz kartę? (T/N): ")
        return odpowiedz == "t"

    def wypad(self):
        print(self.imie_gracza, "odpada.")
        self.przegrana()

    def przegrana(self):
        print(self.imie_gracza, "przegrywa.")

    def wygrana(self):
        print(self.imie_gracza, "wygrywa.")

    def remis(self):
        print(self.imie_gracza, "remisuje")


class BJ_Rozdajacy(BJ_Reka):
    """Rozdający w grze"""
    def dobiera(self):
        return self.total < 17

    def wypad(self):
        print(self.imie_gracza, "odpada.")

    def zakryj_pierwsza_karte(self):
        pierwsza = self.karty[0]
        pierwsza.obroc()


class BJ_Gra(object):
    """Gra w BlackJacka"""
    def __init__(self, imiona):
        self.gracze = []
        for imie in imiona:
            gracz = BJ_Gracz(imie)
            self.gracze.append(gracz)

        self.rozdajacy = BJ_Rozdajacy("Rozdajacy")

        self.talia = BJ_Talia()
        self.talia.zapelnij_talie()
        self.talia.tasuj()

    @property
    def wciaz_w_grze(self):
        wwg = []
        for gracz in self.gracze:
            if not gracz.odpada():
                wwg.append(gracz)
        return wwg

    def __dodatkowe_karty(self, gracz):
        while not gracz.odpada() and gracz.dobiera():
            self.talia.rozdaj([gracz])
            print(gracz)
            if gracz.odpada():
                gracz.wypad()

    def graj(self):
        # rozdaj początkowe 2 karty
        self.talia.rozdaj(self.gracze + [self.rozdajacy], ile_kart=2)
        self.rozdajacy.zakryj_pierwsza_karte() #ukrywa pierwsza karte rozdajacego
        for gracz in self.gracze:
            print(gracz)
        print(self.rozdajacy)

        # rozdaj dodatkowe karty
        for gracz in self.gracze:
            self.__dodatkowe_karty(gracz)

        self.rozdajacy.zakryj_pierwsza_karte() # odsłoń 1 karte rozdającego

        if not self.wciaz_w_grze:
            print(self.rozdajacy)
        else:
            #wydaj dodatkową kartę rozdającemu
            print(self.rozdajacy)
            self.__dodatkowe_karty(self.rozdajacy)

            if self.rozdajacy.odpada():
                # wygrywają gracze pozostający w grze
                for gracz in self.wciaz_w_grze:
                    gracz.wygrana()
            else:
                # porównaj wyniki z rozdającym
                for gracz in self.wciaz_w_grze:
                    if gracz.total > self.rozdajacy.total:
                        gracz.wygrana()
                    elif gracz.total < self.rozdajacy.total:
                        gracz.przegrana()
                    else:
                        gracz.remis()

        # czyść karty wszystkich graczy
        for gracz in self.gracze:
            gracz.czysc_reke()
        self.rozdajacy.czysc_reke()


def main():
    print("Witaj w BlackJack")

    imiona = []
    ilosc_graczy = GryModule.zapytaj_o_liczbe("Podaj ilość uczestników (1-7): ", 1, 8)
    for i in range(ilosc_graczy):
        imie = input("Wprowadź nazwe gracza: ")
        imiona.append(imie)
    print()

    gra = BJ_Gra(imiona)

    ponownie = None
    while ponownie != "n":
        gra.graj()
        ponownie = GryModule.zapytaj_tak_nie("Czy chcesz zagrac ponownie?: ")


main()
input("Aby zakończyć, wciśnij Enter")