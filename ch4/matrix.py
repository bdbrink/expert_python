class Matrix:
    def __init__(self, rows):
        if len(set(len(row) for row in rows)) > 1:
            raise ValueError("All matrix rows must be the same length")
        
        self.rows = rows

    def __add__(self, other):
        if (
            len(self.rows) != len(other.rows) or
            len(self.rows[0]) != len(other.rows[0])
        ):
            raise ValueError("Matrix dimensions don't match")
        
        return Matrix([
            [a + b for a, b in zip(a_row, b_row)]
            for a_row, b_row in zip(self.rows, other.rows)
        ]
        )

    def __sub__(self, other):
        if (
            len(self.rows) != len(other.rows) or
            len(self.rows[0]) != len(other.rows[0])
        ):
            raise ValueError("Matrix dimensions don't match")
        
        return Matrix([
            [a - b for a,b in zip(a_row, b_row)]
            for a_row, b_row in zip(self.rows, other.rows)
        ])