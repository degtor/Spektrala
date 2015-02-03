from Process_data import Process_data
from random import randint

if __name__ == '__main__':
    def __main__():
        place_objects_SW = Process_data('geodataSW.txt')
        place_objects_CH = Process_data('geodataCH.txt')
        n=randint(0, len(place_objects_SW.objects_list))
        print("**SOKNING I SVERIGE**")
        sok_sverige = place_objects_SW.search_place(place_objects_SW.objects_list[n].name)
        n2=randint(0, len(place_objects_CH.objects_list))
        print("**SOKNING I KINA**")
        sok_kina = place_objects_CH.search_place(place_objects_CH.objects_list[n2].name)
        print("Sveriges platser aer sohaer monga: " + str(len(place_objects_SW.objects_list)) + "\nKinas platser aer sohaer monga: " + str(len(place_objects_CH.objects_list)))
__main__()