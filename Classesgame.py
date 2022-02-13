# класс точки
class Dot:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Dot({self.x},{self.y})"
# класс доски
class Board:
    def __init__(self, hide = False, sizes=6):
        self.hide = hide
        self.sizes = sizes
        self.board_list = [[" "]*self.sizes]*self.sizes
    def __str__(self):
        res = "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        res += f"\n----------------------------"
        for i, row in enumerate(self.board_list):
            res += f"\n{i+1} | "+" | " .join(row)+" |"
            res += f"\n----------------------------"
        if self.hide == True:
            res = res.replace("■", " ")
        return res



a = Board()
print(a)
