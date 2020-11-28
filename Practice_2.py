from abc import ABC, abstractmethod


class Wear(ABC):
    @abstractmethod
    def get_cloth(self):
        pass


class Demi_Wear(Wear):
    def __init__(self):
        while True:
            self.name = input('Какую одежду выберетие?\nПальто\nКостюм\n').lower()
            if self.name == 'пальто' or self.name == 'костюм':
                break
            elif self.name == 'exit':
                break
            else:
                print(f'{self.name} - такой одежды нет на выбор\n')
                continue

        self.size = self.name
        self.height = self.name
        self.cloth = self.name

    @property
    def cloth(self):
        return self.__cloth

    @property
    def size(self):
        return self.__size

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, name):
        if name == 'костюм':
            self.__height = float(input(f'Введите рост для {name}: '))
        else:
            self.__height = None

    @size.setter
    def size(self, name):
        if name == 'пальто':
            self.__size = float(input(f'Введите размер для {name}: '))
        else:
            self.__size = None

    @cloth.setter
    def cloth(self, name):
        if name == 'костюм':
            self.__cloth = 2 * self.height + 0.3
        elif name == 'пальто':
            self.__cloth = self.size / 6.5 + 0.5
        else:
            self.__cloth = self.size * self.height

    def get_cloth(self):
        return f'Расход ткани для {self.name} составит: {self.cloth}'


a = Demi_Wear()
print(a.get_cloth())
