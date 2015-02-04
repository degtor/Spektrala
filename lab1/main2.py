from Process_geodata import Process_geodata
from random import randint

if __name__ == '__main__':

    def __main__():
        geodata_SW = Process_geodata('geodataSW.txt')
        geodata_CH = Process_geodata('geodataCH.txt')
        n=randint(0, len(geodata_SW.places))
        print("**SOKNING I SVERIGE**")
        sok_sverige = geodata_SW.search_place(geodata_SW.places[n].name)
        n2=randint(0, len(geodata_CH.places))
        print("**SOKNING I KINA**")
        sok_kina = geodata_CH.search_place(geodata_CH.places[n2].name)
        print("Antal platser i Sverige: " + str(len(geodata_SW.places)) + "\nAntal platser i Kina: " + str(len(geodata_CH.places)))

__main__()