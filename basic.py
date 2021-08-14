
#############################
# TOKEN TYPES
#############################

TT_INT = 'INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'

DIGITS = '0123456789'

class Position(object):

    def __init__(self, idx, ln, col):
        self.idx = idx
        self.ln = ln
        self.col = col

    def advance(self, current_char):
        self.idx +=1
        self.col +=1

        if current_char== '\n':
            self.ln+=1
            self.col=0
            
    def copy(self):
        return Position(self.idx, self.ln, self.col)
      
class Token(object):

    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

class Lexer(object):

    def __init__(self, text):
        self.text = text
        self.pos = Position(-1,0,-1)
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def make_tokens(self):
        tokens=[]

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char in DIGITS +'.':
                tokens.append(self.make_number())
                #self.advance()          
        return tokens

    def make_number(self):
        num_str = ''
        dot_count = 0

        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count==1:
                    break
                else:
                    dot_count=1
                    num_str += '.'
                    self.advance()
            else:
                num_str+=self.current_char
                self.advance()

        if dot_count==0:
            return Token(TT_INT, int(num_str))
        else:
            return Token(TT_FLOAT, float(num_str))


        


    
    
