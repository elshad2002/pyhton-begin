# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
# __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде
# прямоугольной схемы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
# объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой
# строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        line = ""
        result_matrix = ""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                line += f"{self.matrix[i][j]} "
            result_matrix += f"{line}\n"
            line = ""
        return result_matrix

    def __add__(self, other):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return self.matrix


m_1 = Matrix([[1, 4, 5], [5, 7, 6], [8, 9, 0]])
m_2 = Matrix([[1, 6, 5], [5, 7, 6], [8, 9, 0]])
print(m_1)
print(m_2)
m = Matrix(m_1+m_2)
print(m)
