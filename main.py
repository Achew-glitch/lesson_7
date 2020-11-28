class Auto:
    def __init__(self, year_auto):
        self.year = year_auto

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2020:
            self.__year = 2020
        else:
            self.__year = year

    def get_auto_year(self):
        return f'Автомобиль выпущен в {str(self.year)} году'


a = Auto(2090)
print(a.year)
print(a.get_auto_year())
name = 'Suit'.lower()
print(name == 'suit')


class Mine(object):

    def __init__(self, value):
        self._x = value

#    x = property()

    @property
    def x(self):
        """Это свойство x."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        self._x = 'No more'


print(type(Mine.x))
mine = Mine(6)
print(mine.x)
mine.x = 3
print(mine.x)
del mine.x
print(mine.x)
