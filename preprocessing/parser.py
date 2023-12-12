import re

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.current_index = 0

    def parse(self):
        self.advance()
        return self.parse_program()

    def advance(self):
        if self.current_index < len(self.tokens):
            self.current_token = self.tokens[self.current_index]
            self.current_index += 1

    def match(self, expected_type):
        if self.current_token and self.current_token[0] == expected_type:
            self.advance()
        else:
            raise ValueError(f"Expected {expected_type}, found {self.current_token}")

    def parse_program(self):
        self.match('KEYWORD')  # int
        self.match('IDENTIFIER')  # main
        self.match('PUNCTUATION')  # (
        self.match('KEYWORD')  # void
        self.match('PUNCTUATION')  # )
        self.match('PUNCTUATION')  # {
        self.parse_statement()
        self.match('PUNCTUATION')  # }
        return "Parsing successful"

    def parse_statement(self):
        self.match('RETURN')  # return
        self.parse_expression()
        self.match('PUNCTUATION')  # ;
        return "Statement parsed successfully"

    def parse_expression(self):
        self.match('NUMBER')  # 2
        return "Expression parsed successfully"