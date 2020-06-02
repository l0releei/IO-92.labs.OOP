class Tariff:

    def __init__(self, name, price_per_month, sms_amount, minutes_amount, gb_amount):
        self.name = name
        self.price_per_month = price_per_month
        self.sms_amount = sms_amount
        self.minutes_amount = minutes_amount
        self.gb_amount = gb_amount


class TariffForInternet(Tariff):

    def __init__(self, name, price_per_month, sms_amount, minutes_amount):
        super().__init__(name, price_per_month, sms_amount, minutes_amount, 100)

    def __repr__(self):
        return f"""{self.name.capitalize()} offers you:
                   {self.sms_amount} of SMS,
                   {self.minutes_amount} min. of calls
                   and {self.gb_amount}GB of Internet
                   per {self.price_per_month} per month!"""


class TariffForSMS(Tariff):

    def __init__(self, name, price_per_month, minutes_amount, gb_amount):
        super().__init__(name, price_per_month, 1000, minutes_amount, gb_amount)

    def __repr__(self):
        return f"""{self.name} offers you:
                   {self.sms_amount} of SMS,
                   {self.minutes_amount} min. of calls
                   and {self.gb_amount}GB of Internet
                   per {self.price_per_month} per month!"""


class TariffForCalls(Tariff):

    def __init__(self, name, price_per_month, sms_amount, gb_amount):
        super().__init__(name, price_per_month, sms_amount, 6000, gb_amount)

    def __repr__(self):
        return f"""{self.name.capitalize()} offers you:
                   {self.sms_amount} of SMS,
                   {self.minutes_amount} min. of calls
                   and {self.gb_amount}GB of Internet
                   per {self.price_per_month} per month!"""


class Main:
    names = ["Red Tariff", "Orange Tariff", "Yellow Tariff",
             "Green Tariff", "Blue Tariff", "Cyan Tariff",
             "Violet Tariff", "Magenta Tariff", "Pink Tariff"]
    my_tariffs = []

    def __init__(self):
        for i in range(0, 3):
            self.my_tariffs.append(TariffForInternet(name=self.names[i],
                                                     price_per_month=(i + 1) * 40,
                                                     sms_amount=(i + 1) * 50,
                                                     minutes_amount=(i + 1) * 60))
            self.my_tariffs.append(TariffForSMS(name=self.names[i + 3],
                                                price_per_month=(i + 1) * 30,
                                                minutes_amount=(i + 1) * 60,
                                                gb_amount=(i + 2) * 2))
            self.my_tariffs.append(TariffForCalls(name=self.names[i + 6],
                                                  price_per_month=(i + 1) * 20,
                                                  sms_amount=(i + 1) * 50,
                                                  gb_amount=(i + 2) * 2))

    def print_all_tariffs(self):
        for tariff in self.my_tariffs:
            print(tariff)

    def shorted_print(self, tariffs):
        for tariff in tariffs:
            print(tariff.name)

    def sort_by_price(self):
        return sorted(self.my_tariffs, key=lambda tariff: tariff.price_per_month)

    def find_in_price_range(self, more, less):
        return [tariff for tariff in self.my_tariffs if more < tariff.price_per_month < less]


if __name__ == '__main__':
    lab6 = Main()
    lab6.print_all_tariffs()
    print("\nSorted by price:\n")
    lab6.shorted_print(lab6.sort_by_price())
    print("\nPrice\n")
    lab6.shorted_print(lab6.find_in_price_range(50, 100))



