import re


# # lexical analysis
class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.tokens = []

    def tokenize(self):
        while self.position < len(self.source_code):
            char = self.source_code[self.position]

            if char.isspace():
                self.position += 1
            elif char.isalpha():
                identifier = self.extract_identifier()
                self.tokens.append(Token("IDENTIFIER", identifier))
            elif char.isdigit():
                number = self.extract_number()
                self.tokens.append(Token("NUMBER", number))
            elif char == '+':
                self.tokens.append(Token("PLUS", char))
                self.position += 1
            elif char == '-':
                self.tokens.append(Token("MINUS", char))
                self.position += 1
            elif char == '=':
                self.tokens.append(Token("ASSIGN", char))
                self.position += 1
            else:
                raise ValueError(f"Unexpected character: {char}")

        return self.tokens

    def extract_identifier(self):
        identifier = ""
        while self.position < len(self.source_code) and self.source_code[self.position].isalnum():
            identifier += self.source_code[self.position]
            self.position += 1
        return identifier

    def extract_number(self):
        number = ""
        while self.position < len(self.source_code) and self.source_code[self.position].isdigit():
            number += self.source_code[self.position]
            self.position += 1
        return int(number)

# Example usage:
source_code = "x = 42 + y"
lexer = Lexer(source_code)
tokens = lexer.tokenize()
for token in tokens:
    print(f"Type: {token.type}, Value: {token.value}")



## synatx analysis

import re

class Token:
    def __init__(self, token_type, value):
        self.type = token_type
        self.value = value

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code
        self.position = 0
        self.tokens = []

    def tokenize(self):
        while self.position < len(self.source_code):
            char = self.source_code[self.position]

            if char.isspace():
                self.position += 1
            elif char.isalpha():
                identifier = self.extract_identifier()
                self.tokens.append(Token("IDENTIFIER", identifier))
            elif char.isdigit():
                number = self.extract_number()
                self.tokens.append(Token("NUMBER", number))
            elif char == '+':
                self.tokens.append(Token("PLUS", char))
                self.position += 1
            elif char == '-':
                self.tokens.append(Token("MINUS", char))
                self.position += 1
            elif char == '=':
                self.tokens.append(Token("ASSIGN", char))
                self.position += 1
            else:
                raise ValueError(f"Unexpected character: {char}")

        return self.tokens

    def extract_identifier(self):
        identifier = ""
        while self.position < len(self.source_code) and self.source_code[self.position].isalnum():
            identifier += self.source_code[self.position]
            self.position += 1
        return identifier

    def extract_number(self):
        number = ""
        while self.position < len(self.source_code) and self.source_code[self.position].isdigit():
            number += self.source_code[self.position]
            self.position += 1
        return int(number)

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.position = 0

    def advance(self):
        self.position += 1
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
        else:
            self.current_token = None

    def parse(self):
        self.current_token = self.tokens[self.position]
        return self.parse_statement()

    def parse_statement(self):
        if self.current_token.type == "IDENTIFIER":
            variable = self.current_token.value
            self.advance()

            if self.current_token.type == "ASSIGN":
                self.advance()

                if self.current_token.type == "NUMBER":
                    value = self.current_token.value
                    self.advance()
                    return f"AssignStatement({variable}, {value})"
                else:
                    raise ValueError(f"Expected a number after '='")
            else:
                raise ValueError(f"Expected '=' after identifier")
        else:
            raise ValueError(f"Expected an identifier")

# Example usage:
source_code = "x = 42 + y"
lexer = Lexer(source_code)
tokens = lexer.tokenize()

parser = Parser(tokens)
ast = parser.parse()
print(ast)

