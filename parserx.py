
token_index = 0

token_list = [('<KEYWORD>', 'let'), ('<IDENTIFIER>', 'Sum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'A'), ('<PUNCTUATION>', ')'), ('<OPERATOR>', '='), ('<IDENTIFIER>', 'Psum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'A'), ('<PUNCTUATION>', ','), ('<IDENTIFIER>', 'Order'), ('<IDENTIFIER>', 'A'), ('<PUNCTUATION>', ')'), ('<KEYWORD>', 'where'), ('<KEYWORD>', 'rec'), ('<IDENTIFIER>', 'Psum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'T'), ('<PUNCTUATION>', ','), ('<IDENTIFIER>', 'N'), ('<PUNCTUATION>', ')'), ('<OPERATOR>', '='), ('<IDENTIFIER>', 'N'), ('<KEYWORD>', 'eq'), ('<INTEGER>', '0'), ('<OPERATOR>', '->'), ('<INTEGER>', '0'), ('<OPERATOR>', '|'), ('<IDENTIFIER>', 'Psum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'T'), ('<PUNCTUATION>', ','), ('<IDENTIFIER>', 'N'), ('<OPERATOR>', '-'), ('<INTEGER>', '1'), ('<PUNCTUATION>', ')'), ('<OPERATOR>', '+'), ('<IDENTIFIER>', 'T'), ('<IDENTIFIER>', 'N'), ('<KEYWORD>', 'in'), ('<IDENTIFIER>', 'Print'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'Sum'), ('<PUNCTUATION>', '('), ('<INTEGER>', '1'), ('<PUNCTUATION>', ','), ('<INTEGER>', '2'), ('<PUNCTUATION>', ','), ('<INTEGER>', '3'), ('<PUNCTUATION>', ','), ('<INTEGER>', '4'), ('<PUNCTUATION>', ','), ('<INTEGER>', '5'), ('<PUNCTUATION>', ')'), ('<PUNCTUATION>', ')')]

next_token = token_list[token_index ]

def read(token):
    global next_token
    global token_index
    if next_token[1] == token:
        print(f"{token} read success")
        token_index += 1
        next_token = token_list[token_index]
    else:
        print("error")

def parse(token_list):
    global next_token
    global token_index
    token_list.append("$")
    token_index = 0
    next_token = token_list[token_index]
    print(next_token)
    E()

    if next_token == "$":
        print("Parsing successful")
    else:
        print("Error !")


def E():
    if next_token[1]=="let":
        read("let")
        D()
        read("in")
        E()
    elif next_token[1] == "fn":
        read("fn")
        Vb()
        while next_token[0] == "<IDENTIFIER>" or (next_token[0] == "<PUNCTUATION>" and next_token[1] == "("):
            Vb()
        read(".")
        E()
    else:
        Ew()

def D():
    pass


def Vb():
    pass

def Ew():
    T()
    if next_token == "where":
        read(next_token)
        Dr()


def T():
    Ta()
    while (next_token[0] == "<PUNCTUATION>" and next_token[1] == ","):
            read(",")
            Ta()
    



def Ta():
    Tc()
    while next_token == "aug":
        read(next_token)
        Tc()



def Tc():
    B()
    if next_token[0]== "<OPERATOR>" and next_token[1] == "->" :
        Tc()
        read("|")
        Tc()
    



def B():
    Bt()
    if next_token[1] == "or":
        read("or")
        Bt()



def Bt():
    Bs()
    if next_token[1] =="&":
        read("&")
        Bt()


def Bs():
    if next_token[1] =="not" :
        read("not")
    Bp()




def Bp():
    A()
    if next_token[1] =="gr" or next_token[1] == ">":
        read(next_token[1])
        A()
    elif next_token[1] =="ge" or next_token[1] == ">=":
        read(next_token[1])
        A()
    elif next_token[1] =="ls" or next_token[1] == "<":
        read(next_token[1])
        A()
    elif next_token[1] =="le" or next_token[1] == "<=":
        read(next_token[1])
        A()
    elif next_token[1] =="eq":
        read("eq")
        A()
    elif next_token[1] =="ne":
        read("ne")
        A()


def A():#check later
    if next_token[1] == "+" :
        read("+")
        At()
    elif next_token[1] == "-" :
        read("-")
        At()
    else:
        At()
        while next_token[1] in ("+", "-"):
            if next_token[1] == "+" :
                read("+")
                At()
            if next_token[1] == "-" :
                read("-")
                At()

def At():
    Af()
    while next_token[1] in ("*", "/"):
        if next_token[1] == "*" :
            read("*")
            Af()
        if next_token[1] == "/" :
            read("/")
            Af()


def Af():
    Ap()
    if next_token[1] == "**" :
        read("**")
        Af()



def Ap():
    R()

    while next_token[1] == "@" :
        read("@")
        if next_token[0] == "<IDENTIFIER>":
            read(next_token[1])
            R()
        else:
            print("Error parsing Ap")


def R():
    Rn()
    

def Rn():
    pass





def Dr():
    pass
# E()
# print(next_token)