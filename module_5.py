


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors



    def go_to(self,new_floor):
        for i in range( 1, new_floor + 1):
            if 0 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print(f'Такого этажа не существует:{new_floor}')
                break

h1 = House('ЖК Горский',18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
print('----------------------------------')
h2.go_to(10)
print('----------------------------------')