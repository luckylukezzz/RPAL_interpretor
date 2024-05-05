import lex

token_index = 0

token_list = lex.lexMatches()
token_list.append("END")
next_token = token_list[token_index]

dict = {
    "<IDENTIFIER>": "<ID:",
    "<INTEGER>": "<INT:",
    "<STRING>": "<STR:"
}

class Node:
    def __init__(self, token):
        self.token = token
        self.children = []

    def add_child(self, child):
        self.children.insert(0, child)

ast = []

def build_tree(token, arguments):
    # print(f'build_tree {token},{arguments}')
    new_node = Node(token)
    for _ in range(arguments):
        if ast:
            new_node.children.insert(0, ast.pop())
        else:
            print("Stack is empty!")
            raise ValueError("Error")
    ast.append(new_node)

out_ast_list = []

def print_ast(root, depth=0):
    global out_ast_list
    print("." * depth + root.token )
    out_ast_list.append("." * depth + root.token)

    for child in root.children:
        print_ast(child, depth + 1)


def print_ast_to_file(root, depth=0, filename="astout.txt"):
    with open(filename, "a") as file:
        file.write("." * depth + root.token + "\n")

        for child in root.children:
            print_ast_to_file(child, depth + 1, filename)

def read(token):
    global next_token
    global token_index
    if next_token[1] == token:
        # print(f"{token} read success")
        token_index += 1
        next_token = token_list[token_index]
    else:
        print("error")


#Grammer


def E():
    if next_token[1] == "let":
        read("let")
        D()
        read("in")
        E()
        build_tree("let", 2)
    elif next_token[1] == "fn":
        read("fn")
        Vb()
        n=2
        while next_token[0] == "<IDENTIFIER>" or (next_token[0] == "<PUNCTUATION>" and next_token[1] == "("):
            Vb()
            n+=1
        read(".")
        E()
        build_tree("lambda", n)
    else:
        Ew()


def Ew():
    T()
    if next_token[1] == "where":
        read("where")
        Dr()
        build_tree("where", 2)

def T():
    Ta()
    if next_token[1] == ',':
        n=1
        while (next_token[1] == ","):
            read(",")
            Ta()
            n+=1
        build_tree('tau',n)


def Ta():
    Tc()
    while next_token[1] == "aug":
        read("aug")
        Tc()
        build_tree("aug", 2)

def Tc():
    B()
    if (next_token[1] == "->" ):
        read('->')
        Tc()
        read("|")
        Tc()
        build_tree("->", 3)


def B():
    Bt()
    while next_token[1] == "or":
        read("or")
        Bt()
        build_tree("or", 2)


def Bt():
    Bs()
    while next_token[1] == "&":
        read("&")
        Bs()
        build_tree("&", 2)

def Bs():
    if next_token[1] == "not":
        read("not")
        Bp()
        build_tree("not", 1)
    else:
        Bp()


def Bp():
    A()
    if next_token[1] in ["gr",">"]:
        read(next_token[1])
        A()
        build_tree("gr",2)

    elif next_token[1] in ["ge", ">="]:
        read(next_token[1])
        A()
        build_tree("ge", 2)

    elif next_token[1] in ["ls", "<"]:
        read(next_token[1])
        A()
        build_tree("ls", 2)

    elif next_token[1] in ["le", "<="]:
        read(next_token[1])
        A()
        build_tree("le", 2)

    elif next_token[1] in ["eq"]:
        read(next_token[1])
        A()
        build_tree("eq", 2)

    elif next_token[1] in ["ne"]:
        read(next_token[1])
        A()
        build_tree("ne", 2)


def A():
    if next_token[1] == "+":
        read("+")
        At()
    elif next_token[1] == "-":
        read("-")
        At()
        build_tree("neg", 1)
    else:
        At()
        while next_token[1] in ("+", "-"):
            temp = next_token[1]
            read(next_token[1])
            At()
            build_tree(temp, 2)

def At():
    Af()
    while next_token[1] in ("*", "/"):
        temp = next_token[1]
        read(next_token[1])
        Af()
        build_tree(temp,2)

def Af():
    AP()
    if next_token[1] == '**':
        read('**')
        Af()
        build_tree("**", 2)

def AP():
    R()
    while (next_token[1]=='@'):
        read('@')
        build_tree(next_token[1],0)  ##check
        read(next_token[1])
        R()
        build_tree("@", 3)

def R():
    Rn()
    while next_token[0] in ('<IDENTIFIER>','<INTEGER>','<STRING>') or next_token[1] in ('true','false','nil','(','dummy'):
        Rn()
        build_tree("gamma",2)

def Rn():
    if next_token[0] in ('<IDENTIFIER>','<INTEGER>','<STRING>'):
        build_tree(f'{dict[next_token[0]]}{next_token[1]}>',0)
        read(next_token[1])

    elif next_token[1] in ('true','false','nil','dummy') :
        build_tree(next_token[1], 0)
        read(next_token[1])

    elif next_token[1] == '(':
        read('(')
        E()
        read(')')


def D():
    Da()
    if next_token[1]=='within':
        read('within')
        D()
        build_tree('within',2)


def Da():
    Dr()
    if (next_token[1]=='and'):
        read('and')
        Dr()
        n=2
        while (next_token[1]=='and'):
            read('and')
            Dr()
            n+=1
        build_tree('and',n)


def Dr():
    if (next_token[1]=='rec'):
        read('rec')
        Db()
        build_tree('rec',1)

    else:
        Db()


def Db(): #check
    if(next_token[1]=='('):
        read('(')
        D()
        read(')')
    else:
        build_tree(f"{dict[next_token[0]]}{next_token[1]}>",0)
        read(next_token[1])
        if (next_token[0] == '<IDENTIFIER>' or next_token[1]=='('):
            Vb()
            n = 3  # check
            while next_token[0] == '<IDENTIFIER>' or next_token[1] == '(':
                Vb()
                n += 1
            read('=')
            E()
            build_tree("function_form", n)

        else:
            if next_token[1] ==',':
                read(',')
                Vl()
            read('=')
            E()
            build_tree("=", 2)

def Vb():
    if(next_token[0]=='<IDENTIFIER>'):
        build_tree(f"{dict[next_token[0]]}{next_token[1]}>",0)
        read(next_token[1])
    elif next_token[1]=='(':
        read('(')
        if next_token[1]==')':
            read(')')
            build_tree('()',0)
        else:
            Vl()
            read(')')

def Vl():
    build_tree(f"{dict[next_token[0]]}{next_token[1]}>",0)
    read(next_token[1])
    n=1
    while(next_token[1]==','):
        read(',')
        build_tree(f"{dict[next_token[0]]}{next_token[1]}>", 0)
        read(next_token[1])
        n+=1
    if n>1:
        build_tree(',',n)



def getAst():
    E()
    print_ast(ast[0])
    return out_ast_list

