PLUS = 0
MINUS = 1
MUL = 2
DIV = 3
LPAREN = 4
RPAREN = 5
NUMBER = 6 

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        return self.value

