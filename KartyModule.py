class Karty(object):
    RANGA = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Walet", "Dama", "Król", "As"]
    KOLOR = ["pik", "kier", "trefl", "karo"]

# Konstrukcja karty - ranga, kolor i ułożenie jej frontem do góry
    def __init__(self, ranga, kolor, front=True):
        self.ranga = ranga
        self.kolor = kolor
        self.front = front

# Reprezentacja karty
    def __str__(self):
        if self.front:
            pokaz = self.ranga + " " + self.kolor
        else:
            pokaz = "XX"
        return pokaz

# Obracanie karty
    def obroc(self):
        self.front = not self.front


class Reka(object):
    # Karty w reku gracza - konstruktor tworzy pustą listę
    def __init__(self):
        self.karty = []

    # Reprezentacja karty
    def __str__(self):
        if self.karty:
            pokaz = ""
            for karta in self.karty:
                pokaz += str(karta) + ", "
        else:
            pokaz = "Pusta"
        return pokaz

    # Czyszczenie reki z kart
    def czysc_reke(self):
        self.karty = []

    # Dodanie karty do ręki
    def dodaj_karte(self, karta):
        self.karty.append(karta)

    # Przekazanie karty do innej reki
    def oddaj_karte(self, karta, inna_reka):
        self.karty.remove(karta)
        inna_reka.dodaj_karte(karta)


class Talia(Reka):
    # Talia z kartami - konstruktor dziedziczony z klasy Reka tworzy pusta listę
    # Zapełnienie talii kartami
    def zapelnij_talie(self):
        for kolor in Karty.KOLOR:
            for ranga in Karty.RANGA:
                self.dodaj_karte(Karty(ranga, kolor))

    # Tasowanie talii kart
    def tasuj(self):
        import random
        random.shuffle(self.karty)

    # Metoda rozdania kart - Ile do ilu rąk
    def rozdaj(self, rece, ile_kart=1):
        for kolejka in range(ile_kart):
            for reka in rece:
                if self.karty:
                    pierwsza_karta = self.karty[0]
                    self.oddaj_karte(pierwsza_karta, reka)
                else:
                    print("Skończyły się karty w talii")


if __name__ == "__main__":
    print("Moduł zawiera podstawowe klasy do gry w karty.")
    input("\n\nAby zakończyć, nacisnij klawisz ENTER.")
