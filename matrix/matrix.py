from os import linesep
class Matrix(object):
    def __init__(self, matrix_string: str):
        string_rows:[str] = matrix_string.splitlines()
       
        self.matrix = [
            [int(el) for el in string_row.split(' ')] 
                for string_row in string_rows
        ]

    def row(self, index: int):

        return self.matrix[index-1]

    def column(self, index: int):
        return [row[index-1] for row in self.matrix ]
