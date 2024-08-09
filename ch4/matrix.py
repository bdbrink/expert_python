class Matrix:
    def __init__(self, rows):
        if len(set(len(row) for row in rows)) > 1:
            raise ValueError("All matrix rows must be the same length")
        
        self.rows = rows