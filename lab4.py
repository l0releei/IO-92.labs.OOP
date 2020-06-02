import random


class SportsEquipment:

    def __init__(self, name, price, weight, colour, material):
        self.name = name
        self.price = price
        self.weight = weight
        self.colour = colour
        self.material = material

    def __repr__(self):
        return f"This is {self.colour} {self.material} {self.name} that weights {self.weight}g and costs {self.price}$."


class Main:
    equipments = []

    def create_equipments(self):
        names = ["ball", "bike simulator", "jumping-rope", "ping pong table", "tennis racket"]
        colours = ["red", "green", "blue", "silver", "gold"]
        materials = ["rubber", "plastic", "plastic", "wood", "metal"]

        for i in range(5):
            self.equipments.append(SportsEquipment(names[i], (i+1) * 100, (i+2)*200, colours[i], materials[i]))

        random.shuffle(self.equipments)

        for equipment in self.equipments:
            print(equipment)

    def sort_by_price(self):
        # Ascending
        return sorted(self.equipments, key=lambda equipment: equipment.price)

    def sort_by_name(self):
        # Descending
        return sorted(self.equipments, key=lambda equipment: equipment.name, reverse=True)


if __name__ == '__main__':
    Lab4 = Main()
    Lab4.create_equipments()
    print("\n")
    print("Сортировка цен за возрастанием:\n", Lab4.sort_by_price())
    print("Сортировка имен за алфавитом:\n", Lab4.sort_by_name())
