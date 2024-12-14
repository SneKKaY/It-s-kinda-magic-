class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("The floor doesn't exist")
        else:
            for i in range(new_floor):
                print(i+1)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, количество этажей {self.number_of_floors} '

    def __eq__(self, other):
        isinstance(other, House)
        return self.number_of_floors == other

    def __lt__(self, other):
        isinstance(other, House)
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        isinstance(other, House)
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        isinstance(other, House)
        return self.number_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        isinstance(other, House)
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        isinstance(other, House)
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        isinstance(value, House)
        return self.number_of_floors + value

    def __radd__(self, value):
        isinstance(value, House)
        return self.number_of_floors + value

    def __iadd__(self, value):
        isinstance(value, House)
        return self.number_of_floors + value


h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)



print(h1)

print(h2)



print(h1 == h2) # __eq__



h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)



h1 += 10 # __iadd__

print(h1)



h2 = 10 + h2 # __radd__

print(h2)



print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__