class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([str(itm) for itm in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Ошибка размерностей матриц'


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [['5', '7', '23'], ['9', '23', '-54'], ['12', '3', '16']]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2

print(mtrx_1)
print('#' * 30)
print(mtrx_2)
print('#' * 30)
print(mtrx_1 + mtrx_2)
print('#' * 30)
print(new_m)
m_3 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_4 = [['5', '7', '23'], ['9', '-54'], ['12', '3', '16']]
print('#' * 30)
mtrx_3 = Matrix(m_3)
mtrx_4 = Matrix(m_4)
print(mtrx_3 + mtrx_4)
print('#' * 30)
m_3 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_4 = [['5', '7', '23'], ['12', '3', '16'], ['12', '3']]
print(mtrx_3 + mtrx_4)