import re
from tokens import *

operators = [('+', PLUS), ('-', MINUS), ('*', MUL), ('/', DIV), ('(', LPAREN), 
             (')', RPAREN)] 

def match_number(source):
    match = re.search(r'^[0-9]+(\.[0-9]+)?', source)

    if match:
        return Token(NUMBER, match.group(0))

    return None

def match_operators(source):
    for operator in operators:
        op, name = operator 

        match = re.search(r'^\{}'.format(op), source)

        if match:
            return Token(name, match.group(0))

    return None
