from nursery import Nursery
from pet import Pet
from beast_of_burden import BeastOfBurden

def main():
    nursery = Nursery()

    nursery.add_animal(Pet('Барсик', 5, 30, 'Собака'))
    nursery.add_animal(Pet('Мурзик', 3, 10, 'Кошка'))

    nursery.add_animal(BeastOfBurden('Осел', 8, 500, 200))
    nursery.add_animal(BeastOfBurden('Пони', 7, 600, 250))

    for animal in nursery.get_all_animals():
        print(animal)

if __name__ == '__main__':
    main()
