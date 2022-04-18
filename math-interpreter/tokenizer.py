from match import *
from utils import isnewline

match_funcs = [match_number, match_operators]

class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.cursor = 0
        self.line = 1

    def source_length(self):
        return len(self.source)

    def end_of_line(self):
        return self.cursor >= self.source_length()

    def current_char(self):
        return self.source[self.cursor]

    def increment_line(self):
        self.line += 1

    def advance_cursor(self, offset=1):
        self.cursor += offset

    def remaining_source(self):
        return self.source[self.cursor:]

    def ignore_whitespaces(self):
        while not self.end_of_line() and self.current_char().isspace():
            if isnewline(self.current_char()):
                self.increment_line()
            
            self.advance_cursor()

    def match_token(self):
        for match_func in match_funcs:
            token = match_func(self.remaining_source())

            if token:
                return token

        return None

    def next_token(self):
        if self.end_of_line():
            return None

        self.ignore_whitespaces()
        
        token = self.match_token()

        if not token:
            raise Exception('Unexpected token: "{}", line: {}, column: {}'.format(
                self.remaining_source(), self.line, self.cursor))

        self.advance_cursor(len(token.value))

        return token
