class Matrix:
    def __init__(self, xy=[[]]):
        self.matrix = xy

    def __str__(self):
        s = ''
        for el in self.matrix:
            s += f'{el}\n'
        return s

    def __add__(self, other):
        sum_matrix = []
        ind = 0
        if len(other.matrix) == len(self.matrix):
            while ind < len(other.matrix):
                sum_matrix.append([])
                if len(other.matrix[ind]) == len(self.matrix[ind]):
                    ind_2 = 0
                    while ind_2 < len(self.matrix[ind]):
                        sum_matrix[ind].append(self.matrix[ind][ind_2] + other.matrix[ind][ind_2])
                        ind_2 += 1
                    ind += 1
                else:
                    print('Матрицы разных размеров')
        else:
            print('Матрицы разных размеров')

        return Matrix(sum_matrix)


m = Matrix([[1, 2], [3, 4], [5, 6]])
n = Matrix([[5, 6], [7, 8], [9, 10]])
print(n + m)
