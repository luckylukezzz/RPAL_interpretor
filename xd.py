import re

def tokenize(code):
    tokens = []
    while code:
        if code.startswith('//'):  # Comment
            match = re.match(r'//([^\\\n]*)(\\\n)?', code)
            if match:
                #tokens.append(('<DELETE>', '<COMMENT>'))
                code = code[len(match.group(0)):]
            else:
                # If there's a syntax error in the comment, stop parsing
                break

        elif code[0].isalpha() or code[0] == '_':  # Identifier
            match = re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', code)
            if match:
                tokens.append(('<IDENTIFIER>', match.group(0)))
                code = code[len(match.group(0)):]

        elif code[0].isdigit():  # Integer
            match = re.match(r'\d+', code)
            if match:
                tokens.append(('<INTEGER>', match.group(0)))
                code = code[len(match.group(0)):]

        elif code[0] in "+-*/%=":  # Operator
            match = re.match(r'[\+\-\*/%=]+', code)
            if match:
                tokens.append(('<OPERATOR>', match.group(0)))
                code = code[len(match.group(0)):]

        elif code.startswith("''"):  # String
            match = re.match(r"''.*?''", code, re.DOTALL)
            if match:
                tokens.append(('<STRING>', match.group(0)))
                code = code[len(match.group(0)):]

        elif code[0] in ' \t\n':  # Spaces
            match = re.match(r'[ \t\n]+', code)
            if match:
                #tokens.append(('<DELETE>', match.group(0)))
                code = code[len(match.group(0)):]

        elif code[0] in '();,':  # Punctuation
            tokens.append((code[0], code[0]))
            code = code[1:]
        else:
            code = code[1:]  # error

    return tokens

# Example usage:
code = """
// This is a comment
variable_name = 123 + 456;
// This is a \ncomment
string_var = '''This is a multiline

string with special characters: \\t \\n \\' \\''';
"""
tokens = tokenize(code)
for token, match in tokens:
    print(token, match)