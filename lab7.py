from OOP.lab6 import *


class ListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def get_next(self):
        return self.next

    def set_next(self, n):
        self.next = n

    def set_data(self, data):
        if isinstance(data, tuple(Tariff.__subclasses__())):
            self.data = data
        else:
            raise TypeError

    def get_data(self, key=None):
        if key is None:
            return self.data
        else:
            return self.data[key]


class OneLinkedListOfTariffs:

    def __init__(self):
        self.len = 0
        self.head = None
        self.tail = None
        self.tariffs = []

    def show_tariffs(self):
        if self.tariffs:
            print(f"This company offers you:")
            for tariff in self.tariffs:
                print(tariff.data.name)
        else:
            print(f"Currently this company offers you nothing.")

    def add(self, *tariffs):
        for tariff in tariffs:
            new_node = ListNode(data=tariff, next=None)
            self.tariffs.append(new_node)
            if self.head is None:  # if no tariffs
                self.head = self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.len += 1

    def remove(self, *names):
        for name in names:
            current = self.head
            previous = None
            found = False
            while current and found is False:
                if current.get_data().name == name:
                    found = True
                else:
                    previous = current
                    current = current.get_next()
            if current is None:
                raise ValueError("Data not in list")
            if previous is None:
                self.head = current.get_next()
            else:
                previous.set_next(current.get_next())
            self.len -= 1

    def size(self):
        return str(self.len)

    def print_by_index(self, *indexes):
        for index in indexes:
            print(self.tariffs[index].get_data())


if __name__ == '__main__':
    colours = ['White Tariff', 'Yellow Tariff', 'Blue Tariff', 'Red Tariff', 'Green Tariff',
               'Black Tariff', 'Brown Tariff', 'Azure Tariff', 'Ivory Tariff', 'Teal Tariff',
               'Silver Tariff', 'Purple Tariff', 'Navy blue Tariff', 'Pea green Tariff',
               'Gray Tariff', 'Orange Tariff', 'Maroon Tariff', 'Charcoal Tariff', 'Aquamarine Tariff',
               'Coral Tariff', 'Fuchsia Tariff', 'Wheat Tariff', 'Lime Tariff', 'Crimson Tariff', 'Khaki Tariff',
               'Hot pink Tariff', 'Magenta Tariff', 'Olden Tariff', 'Plum Tariff', 'Olive Tariff', 'Cyan Tariff']

    Vodafone = OneLinkedListOfTariffs()
    Kyivstar = OneLinkedListOfTariffs()

    names_for_Vodafone = colours[:len(colours) // 2]

    for i in range(len(names_for_Vodafone) // 3):
        Vodafone.add(TariffForInternet(name=names_for_Vodafone[i],
                                       price_per_month=(i + 1) * 40,
                                       sms_amount=(i + 1) * 50,
                                       minutes_amount=(i + 1) * 60))

        Vodafone.add(TariffForSMS(name=names_for_Vodafone[i + 3],
                                  price_per_month=(i + 1) * 30,
                                  minutes_amount=(i + 1) * 60,
                                  gb_amount=(i + 2) * 2))

        Vodafone.add(TariffForCalls(name=names_for_Vodafone[i + 6],
                                    price_per_month=(i + 1) * 20,
                                    sms_amount=(i + 1) * 50,
                                    gb_amount=(i + 2) * 2))

    Vodafone.show_tariffs()
    print(Vodafone.size())
    Vodafone.print_by_index(10, 4, 0)
    Vodafone.remove('Yellow Tariff', 'Blue Tariff', 'Red Tariff', 'Green Tariff')
    Vodafone.show_tariffs()
    print(Vodafone.size())
