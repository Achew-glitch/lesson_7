class Cell:
    def __init__(self, cells):
        self.cells = int(cells)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            return Cell(abs(self.cells - other.cells))
        else:
            print(f'Вторая клетка содержит больше ячеек.\nВычитание невозможно.')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def __str__(self):
        return f'{self.cells}'

    def make_order(self, order_cells):
        order_str = ''
        ind_c = 1
        while ind_c <= self.cells:
            if ind_c % order_cells == 0:
                order_str += '*\n'
            else:
                order_str += '*'
            ind_c +=1
        return f'Порядок клеток с распределнием по колчиеству {order_cells} в ряду для экземпляра класса {self}:\n{order_str}'


a = Cell(10)
b = Cell(8)
print(a + b)
print(b - a)
print(a - b)
print(a * b)
print(a / b)
print(a.make_order(3))