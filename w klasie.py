class Colors():
    def __init__(self, kolor):
        self.kolor = kolor

        #slownik z kolorami, teraz tylko 1 dla testow
    _przykladowe_kolory = {
        "Red" : "#e6194B"
    }

    def to_hex(self, kolor_key):
        if kolor_key in self._przykladowe_kolory.keys():
            for kolor_key, HEX in self._przykladowe_kolory.items():
                print(HEX)
        else: print("Nie ma w slowniku")


czerwony = Colors("czerwony")
print(czerwony)

czerwony.to_hex(kolor_key="Red")
 
