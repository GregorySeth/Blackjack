class Gracz(object):
    # Uczestnik gry
    def __init__(self, imie, punkty = 0):
        self.imie = imie
        self.punkty = punkty

    def __str__(self):
        pokaz = self.imie + ":\t" + str(self.punkty)
        return pokaz


def zapytaj_tak_nie(pytanie):
    # Zadaj pytnie na ktore mozna odpowiedzieć "tak" lub "nie"
    odpowiedz = None
    while odpowiedz not in ("t", "n"):
        odpowiedz = input(pytanie).lower()
    return odpowiedz


def zapytaj_o_liczbe(pytanie, minimum, maksimum):
    # Poproś o podanie liczby z zakresu
    odpowiedz = None
    while odpowiedz not in range (minimum, maksimum):
        odpowiedz = int(input(pytanie))
    return odpowiedz


if __name__ == "__main__":
    print("Moduł zawiera podstawowe klasy do gry w karty.")
    input("\n\nAby zakończyć, nacisnij klawisz ENTER.")