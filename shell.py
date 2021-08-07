import basic

def run(text):
    lexer = basic.Lexer(text)
    tokens = lexer.make_tokens()
    return tokens

while True:
    text = input('basic > ')
    result = run(text)

    print(result)
