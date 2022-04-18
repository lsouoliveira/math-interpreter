from tokenizer import Tokenizer
from parser import Parser
from interpreter import MathInterpreter

def parse_expression(expression):
    tokenizer = Tokenizer(expression)
    parser = Parser(tokenizer)
    interpreter = MathInterpreter(parser)

    return interpreter.evaluate()

def main():
    try:
        while True:
            expr = input('>> ')

            if len(expr) == 0:
                continue

            try:
                print(parse_expression(expr))
            except Exception as e:
                print('Syntax error')
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
