class AST:
    def __init__(self):

        self.tree_progress = []

    def push_to_tree_progress(self,lvl, item):
        self.tree_progress.append((lvl , item))

    def print_tree_progress(self):
        print("Tree Progress:")
        for item in self.tree_progress:
            print("."*item[0] , item[1])


ast = AST()
        
# def parse(token_list):
#     global next_token
#     global token_index
#     token_list.append("$")
#     token_index = 0
#     next_token = token_list[token_index]
#     print(next_token)
#     E()

#     if next_token == "$":
#         print("Parsing successful")
#     else:
#         print("Error !")


token_index = 0

token_list = [('<KEYWORD>', 'let'), ('<IDENTIFIER>', 'Sum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'A'), ('<PUNCTUATION>', ')'), ('<OPERATOR>', '='), ('<IDENTIFIER>', 'Psum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'A'), ('<PUNCTUATION>', ','), ('<IDENTIFIER>', 'Order'), ('<IDENTIFIER>', 'A'), ('<PUNCTUATION>', ')'), ('<KEYWORD>', 'where'), ('<KEYWORD>', 'rec'), ('<IDENTIFIER>', 'Psum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'T'), ('<PUNCTUATION>', ','), ('<IDENTIFIER>', 'N'), ('<PUNCTUATION>', ')'), ('<OPERATOR>', '='), ('<IDENTIFIER>', 'N'), ('<KEYWORD>', 'eq'), ('<INTEGER>', '0'), ('<OPERATOR>', '->'), ('<INTEGER>', '0'), ('<OPERATOR>', '|'), ('<IDENTIFIER>', 'Psum'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'T'), ('<PUNCTUATION>', ','), ('<IDENTIFIER>', 'N'), ('<OPERATOR>', '-'), ('<INTEGER>', '1'), ('<PUNCTUATION>', ')'), ('<OPERATOR>', '+'), ('<IDENTIFIER>', 'T'), ('<IDENTIFIER>', 'N'), ('<KEYWORD>', 'in'), ('<IDENTIFIER>', 'Print'), ('<PUNCTUATION>', '('), ('<IDENTIFIER>', 'Sum'), ('<PUNCTUATION>', '('), ('<INTEGER>', '1'), ('<PUNCTUATION>', ','), ('<INTEGER>', '2'), ('<PUNCTUATION>', ','), ('<INTEGER>', '3'), ('<PUNCTUATION>', ','), ('<INTEGER>', '4'), ('<PUNCTUATION>', ','), ('<INTEGER>', '5'), ('<PUNCTUATION>', ')'), ('<PUNCTUATION>', ')')]
token_list.append("END")
next_token = token_list[token_index ]


def read(x,token):
    global next_token
    global token_index
    if next_token[1] == token:
        print(f"{token} read success")
        if next_token[0] == "<IDENTIFIER>":
            ast.push_to_tree_progress(x, f"<ID:{next_token[1]}>")
        elif next_token[0] == "<INTEGER>":
            ast.push_to_tree_progress(x, f"<INT:{next_token[1]}>")
        elif next_token[0] == "<STRING>":
            ast.push_to_tree_progress(x, f"<STR:{next_token[1]}>")
        token_index += 1
        next_token = token_list[token_index]
        
    else:
        print("error")





def E(x):

    if next_token[1]=="let":
        ast.push_to_tree_progress(x, "let")
        read(x,"let")
        D(x+1)
        read(x,"in")
        E(x+1)
    elif next_token[1] == "fn":
        ast.push_to_tree_progress(x, "lambda")
        read(x,"fn")
        Vb(x+1)
        while next_token[0] == "<IDENTIFIER>" or (next_token[0] == "<PUNCTUATION>" and next_token[1] == "("):
            Vb(x+1)
        read(x,".")
        E(x+1)
    else:
        Ew(x+1)



def Ew(x):
    T(x+1)
    if next_token[1] == "where":
        ast.push_to_tree_progress(x, "where")
        read(x,"where")
        Dr(x+1)


def T(x):
    Ta(x+1)
    if next_token[1] == ",":
        ast.push_to_tree_progress(x, "tau")
        while (next_token[0] == "<PUNCTUATION>" and next_token[1] == ","):
            read(x,",")
            Ta(x+1)




def Ta(x):
    Tc(x+1)
    if next_token[1] == "aug":
        ast.push_to_tree_progress(x, "aug")
        while next_token[1] == "aug":
            read(x,"aug")
            Tc(x+1)



def Tc(x):
    
    B(x+1)

    if next_token[0]== "<OPERATOR>" and next_token[1] == "->" :
        ast.push_to_tree_progress(x, "->")
        read(x,"->")
        Tc(x+1)
        read(x,"|")
        Tc(x+1)
    



def B(x):
    Bt(x+1)
    if next_token[1] == "or":
        ast.push_to_tree_progress(x, "or")
        read(x,"or")
        Bt(x+1)



def Bt(x):
    Bs(x+1)
    if next_token[1] =="&":
        ast.push_to_tree_progress(x, "&")
        read(x,"&")
        Bt(x+1)


def Bs(x):
    if next_token[1] =="not" :
        ast.push_to_tree_progress(x, "not")
        read(x,"not")
    Bp(x+1)




def Bp(x):
    A(x+1)
    if next_token[1] =="gr" or next_token[1] == ">":
        ast.push_to_tree_progress(x, "gr")
        read(x,next_token[1])
        A(x+1)
    elif next_token[1] =="ge" or next_token[1] == ">=":
        ast.push_to_tree_progress(x, "ge")
        read(x,next_token[1])
        A(x+1)
    elif next_token[1] =="ls" or next_token[1] == "<":
        ast.push_to_tree_progress(x, "ls")
        read(x,next_token[1])
        A(x+1)
    elif next_token[1] =="le" or next_token[1] == "<=":
        ast.push_to_tree_progress(x, "le")
        read(x,next_token[1])
        A(x+1)
    elif next_token[1] =="eq":
        ast.push_to_tree_progress(x, "eq")
        read(x,"eq")
        A(x+1)
    elif next_token[1] =="ne":
        ast.push_to_tree_progress(x, "ne")
        read(x,"ne")
        A(x+1)


def A(x):#check later
    if next_token[1] == "+" :
        read(x,"+")
        At(x+1)
    elif next_token[1] == "-" :
        ast.push_to_tree_progress(x, "neg")
        read(x,"-")
        At(x+1)
    else:
        At(x+1)
        n=x+1
        while next_token[1] in ("+", "-"):
            if next_token[1] == "+" :
                ast.push_to_tree_progress(n-1, "+")
                read(n,"+")
                At(n)
            elif next_token[1] == "-" :
                ast.push_to_tree_progress(n-1, "-")
                read(n,"-")
                At(n)
            n=n+1


def At(x):
    Af(x+1)
    n=x+1
    while next_token[1] in ("*", "/"):
        if next_token[1] == "*" :
            ast.push_to_tree_progress(n-1, "*")
            read(n,"*")
            Af(n)
        if next_token[1] == "/" :
            ast.push_to_tree_progress(n-1, "/")
            read(n,"/")
            Af(n)
        n=n+1

def Af(x):
    Ap(x+1)
    if next_token[1] == "**" :
        ast.push_to_tree_progress(x, "/")
        read(x,"**")
        Af(x+1)



def Ap(x):
    R(x+1)
    n=x+1
    while next_token[1] == "@" :
        ast.push_to_tree_progress(n-1, "@")
        read(n-1,"@")
        if next_token[0] == "<IDENTIFIER>":
            read(n-1,next_token[1])
            R(n)
        else:
            print("Error parsing Ap")
        n=n+1

def R(x):
    Rn(x+1)
    n=x+1
    while next_token[0] in ("<IDENTIFIER>", "<INTEGER>", "<STRING>") or next_token[1] in ('true','false','nil','(',"dummy"):
        ast.push_to_tree_progress(n-1, "gamma")
        Rn(n)
        n=n+1


def Rn(x):
    if next_token[1] == "true":
        ast.push_to_tree_progress(x, "true")
        read(x,"true")
    
    elif next_token[1] == "false":
        ast.push_to_tree_progress(x, "false")
        read(x,"false")

    elif next_token[1] == "nil":
        ast.push_to_tree_progress(x, "nil")
        read(x,"nil")

    elif next_token[1] == "dummy":
        ast.push_to_tree_progress(x, "dummy")
        read(x,"dummy")
    
    elif next_token[0] in ("<IDENTIFIER>", "<INTEGER>", "<STRING>"):
        read(x,next_token[1])

    elif next_token[1] == "(":
        read(x,"(")
        E(x+1)
        read(x,")")
    else:
        pass




def D(x):
    Da(x+1)
    if next_token[1] == "within" :
        ast.push_to_tree_progress(x, "within")
        read(x,"within")
        D(x+1)


def Da(x):
    Dr(x+1)

    if next_token[1] == "and" :
        ast.push_to_tree_progress(x, "and")
        while next_token[1] == "and" :
            read(x,"and")
            Dr(x+1)


def Dr(x):
    if next_token[1] == "rec":
        ast.push_to_tree_progress(x, "rec")
        read(x,"rec")
        Db(x+1)

    else:
        Db(x+1)

def Db(x):
    if next_token[0] == "<IDENTIFIER>":
        ast.push_to_tree_progress(x, "fcn_form")
        read(x,next_token[1])
        if next_token[0] == "<IDENTIFIER>" or  next_token[1] == "(":
            Vb(x+1)

        while next_token[0] == "<IDENTIFIER>" or next_token[1] == "(":
            Vb(x+1)

        if  next_token[1] == "=":
            read(x,"=")
            E(x+1)
            
        else:
            print("Error in Db")
    
    elif next_token[1] == "(":
        read(x,"(")
        D(x+1)
        read(x,")")

    else:
        ast.push_to_tree_progress(x, "=")
        Vl(x+1)
        read(x,"=")
        E(x+1)


def Vb(x):
    if next_token[0] == "<IDENTIFIER>":
        read(x,next_token[1])

    elif next_token[1] == "(":
        read(x,"(")

        if next_token[0] == "<IDENTIFIER>" :
            Vl(x+1)
            read(x,")")
        elif next_token[0] == ")":
                ast.push_to_tree_progress(x, "()")
                read(x,")")
        
    else:
        print("error in Vb")



def Vl(x):
    count =0
    if next_token[0] == "<IDENTIFIER>":
        ast.push_to_tree_progress(x, ",")
        while next_token[0] == "<IDENTIFIER>":
            read(x,next_token[1])
            count = count +1
            if next_token[1] == ",":
                read(x,",")
            
            elif next_token[0] == "<IDENTIFIER>" :
                print("error in Vl")


    if count == 0 :
        print("error in Vl")



E(0)
print(next_token)
ast.print_tree_progress()