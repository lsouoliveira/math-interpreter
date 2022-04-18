from tokens import *

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
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer

    def parse(self):
        self.current_token = self.tokenizer.next_token()

        return self.expr()

    def eat(self, token_type):
        if self.current_token_type() == token_type:
            self.current_token = self.tokenizer.next_token()
        else:
            raise Exception("Expected {} but got {}".format(token_type, 
                self.current_token.type))

    def current_token_type(self):
        if self.current_token != None:
            return self.current_token.type
        
        return None

    def factor(self):
        node = None
        root_sign_node = None
        sign_node = None

        while self.current_token_type() in [PLUS, MINUS]:
            current_token = self.current_token
            self.eat(self.current_token_type())

            root_sign_node = BinaryOperatorNode(NumberNode(Token(NUMBER, 0)),
                    current_token, root_sign_node)

            if not sign_node:
                sign_node = root_sign_node

        if self.current_token_type() == NUMBER:
            number_token = self.current_token
            self.eat(NUMBER)

            node = NumberNode(number_token)
        elif self.current_token_type() == LPAREN:
            self.eat(LPAREN)
            node = self._expr()
            self.eat(RPAREN)

        if not node:
            raise Exception('Expected a number or parentheses, but got {}'.format(
                self.current_token))

        if sign_node:
            sign_node.right = node

            return root_sign_node

        return node

    def term(self):
        node = self.factor()

        while self.current_token_type() in [MUL, DIV]:
            current_token = self.current_token
            self.eat(self.current_token_type())

            node = BinaryOperatorNode(node, current_token, self.factor())

        return node

    def _expr(self):
        node = self.term()

        while self.current_token_type() in [PLUS, MINUS]:
            current_token = self.current_token
            self.eat(self.current_token_type())

            node = BinaryOperatorNode(node, current_token, self.term())

        return node

    def expr(self):
        expr = self._expr()

        if self.current_token:
            raise Exception('Expected + or - but got {}'.format(self.current_token))

        return expr
