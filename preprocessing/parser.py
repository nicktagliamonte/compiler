class ASTNode:
    def __init__(self, node_type, value=None, children=None):
        self.node_type = node_type
        self.value = value
        self.children = children if children is not None else []

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
        node = ASTNode('Program')
        self.match('KEYWORD')  # int
        self.match('IDENTIFIER')  # main
        self.match('PUNCTUATION')  # (
        self.match('KEYWORD')  # void
        self.match('PUNCTUATION')  # )
        self.match('PUNCTUATION')  # {
        node.children.append(self.parse_statement())
        self.match('PUNCTUATION')  # }
        return node

    def parse_statement(self):
        node = ASTNode('Statement')
        self.match('RETURN')  # return
        node.children.append(self.parse_expression())
        self.match('PUNCTUATION')  # ;
        return node

    def parse_expression(self):
        node = ASTNode('Expression', value=self.current_token[1] if self.current_token[0] == 'NUMBER' else None)
        self.match('NUMBER')  # 2 (for simplicity)
        return node