# Измените класс Person так, чтобы его методы 
# оперировали внутренним состоянием, 
# а не использовали цепочку вызовов объектов

class Person:
    def __init__(self, adress: dict):
        self.adress = adress

    def get_person_room(self):
        return self.adress["room"]

    def get_city_population(self):
        return self.adress["city"]["population"]


if __name__ == '__main__':
    adress = {
        'planet': "",
        'contry': "",
        'city': {'name': "", 'population': 100500},
        'street': "",
        'room': 42
    }
    person = Person(adress)

    print(person.get_person_room(), person.get_city_population())

# TODO после выполнения задания попробуйте
# сделать экземпляр класса person и вызвать новые методы.