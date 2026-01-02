class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list:
        diagonal_list = []
        for index in range(len(self.matrix)):
            diagonal_list.append(self.matrix[index][index])
        return diagonal_list

    def get_counter_diagonal(self) -> list:
        counter_diagonal_list = []
        for index in range(len(self.matrix)):
            counter_diagonal_list.append(self.matrix[index][len(self.matrix) - 1 - index])
        return counter_diagonal_list

    def rotate_rows(self, number: int) -> list:
        if not self.matrix:
            return self.matrix

        num_rows = len(self.matrix)
        rotated_rows_list = [None] * num_rows

        for index in range(num_rows):
            new_index = (index - number) % num_rows
            rotated_rows_list[new_index] = self.matrix[index]

        self.matrix = rotated_rows_list
        return self.matrix

    def rotate_columns(self, number: int) -> list:
        if not self.matrix or not self.matrix[0]:
            return self.matrix

        num_rows = len(self.matrix)
        num_cols = len(self.matrix[0])

        rotated = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        print(rotated)
        for row in range(num_rows):
            for col in range(num_cols):
                new_col = (col - number) % num_cols
                rotated[row][new_col] = self.matrix[row][col]

        self.matrix = rotated
        return self.matrix




"""matrix_inst = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]"""

matrix_inst = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

matrix_inst.rotate_columns(1)

"""print(matrix_inst[-1])
print(matrix_inst[-2])
var = list(range(len(matrix_inst)))
print(var)
print([range(len(matrix_inst))])"""

