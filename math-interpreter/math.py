from tokenizer import Tokenizer
from tokens import *

"""
<expr> ::= <term> <stmts>
<stmts> ::= (+ | -) <term> <stmts> | <empty>
<term> ::= <factor> <term_stmts> 
<term_stmts> ::= (* | /) <factor> <term_stmts> | <empty>
<factor> ::= (+ | - | empty) number | lparen <expr> rparen
"""

class Node:
    pass

class BinaryOperatorNode(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op.value
        self.right = right

    def __str__(self):
        return str(self.op)

class NumberNode(Node):
    def __init__(self, token):
        self.value = float(token.value)

    def __str__(self):
        return str(self.value)

class Parser:
    def parse(self, source):
        self.tokenizer = Tokenizer(source)

        self.current_token = self.tokenizer.next_token()

        return self.expr()

    def eat(self, token_type):
        if self.current_token_type() == token_type:
            self.current_token = self.tokenizer.next_token()
        else:
            raise Exception("Expected {} but got {}".format(token_type, self.current_token.type))

    def current_token_type(self):
        if self.current_token != None:
            return self.current_token.type
        
        return None

    def factor(self):
        if self.current_token_type() in [PLUS, MINUS]:
            operator_token = self.current_token
            self.eat(self.current_token_type())

            number_token = self.current_token
            self.eat(NUMBER)

            return BinaryOperatorNode(NumberNode(Token(NUMBER, 0)), operator_token, NumberNode(number_token))
        if self.current_token_type() == NUMBER:
            number_token = self.current_token
            self.eat(NUMBER)

            return NumberNode(number_token)
        elif self.current_token_type() == LPAREN:
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)

            return node

        raise Exception('Expected a number or parentheses, but got {}'.format(self.current_token))

    def term_stmts(self):
        if self.current_token_type() in [MUL, DIV]:
            current_token = self.current_token
            self.eat(self.current_token_type())

            node = BinaryOperatorNode(None, current_token, None)
            factor_node = self.factor()
            stmts2_node = self.term_stmts()

            if stmts2_node:
                stmts2_node.left = factor_node
                node.right = stmts2_node
            else:
                node.right = factor_node

            return node

        return None

    def term(self):
        node = self.factor()

        binary_operator_node = self.term_stmts()

        if binary_operator_node:
            binary_operator_node.left = node

            return binary_operator_node

        return node

    def stmts(self):
        if self.current_token_type() in [PLUS, MINUS]:
            print(self.current_token_type())
            current_token = self.current_token
            self.eat(self.current_token_type())

            node = BinaryOperatorNode(None, current_token, None)
            factor_node = self.term()
            stmts_node = self.stmts()

            if stmts_node:
                stmts_node.left = factor_node
                node.right = stmts_node
            else:
                node.right = factor_node

            return node
        
        return None

    def expr(self):
        node = self.term()

        print(node)

        binary_operator_node = self.stmts()
        if binary_operator_node:
            binary_operator_node.left = node

            return binary_operator_node

        return node

def visit(node):
    if node is None:
        return '[none]'

    if isinstance(node, BinaryOperatorNode):
        return '{}, {}, {}'.format(node.op, visit(node.left), visit(node.right))
    elif isinstance(node, NumberNode):
        return str(node.value)

def visit_calc(node):
    if node is None:
        return 0 

    if isinstance(node, BinaryOperatorNode):
        if node.op == '+':
            return visit_calc(node.left) + visit_calc(node.right)
        elif node.op == '-':
            return visit_calc(node.left) - visit_calc(node.right)
        elif node.op == '*':
            return visit_calc(node.left) * visit_calc(node.right)
        elif node.op == '/':
            return visit_calc(node.left) / visit_calc(node.right)
    elif isinstance(node, NumberNode):
        return node.value 

expr = '3 + 2 * 3'

parser = Parser()
# print(visit(parser.parse(expr)))
# print(visit_calc(parser.parse(expr)))
