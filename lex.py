
import re

list1=[]


with open('filename.txt', 'r') as file:

    text = file.read()
    length = len(text)

    matches= []

    digit = "[0-9]"
    letter = "[a-zA-Z]"
    operatorSymbol = "[+\\-*/<>&.@/:=~|$!#%^_\\[\\]{}`'\\?]"

    identifierPattern = re.compile(f"^{letter}({letter}|{digit}|_)*")
    integerPattern = re.compile(f"{digit}+")
    operatorPattern = re.compile(f"^{operatorSymbol}+")
    punctuationPattern = re.compile("[(),;]")
    spacesPattern = re.compile(r"^(\s|\t)+")
    stringPattern = re.compile(r'^\".*?\"')
    commentPattern = re.compile("^//.*")


    current =0 

    while current < length:
        matcher = spacesPattern.match(text[current:])
        if matcher:
            #matches.append(("space",current))
            current += len(matcher.group())
            continue
        
        matcher = commentPattern.match(text[current:])
        if matcher:
            #matches.append(("comment",current,matcher.group()))
            current += len(matcher.group())
            continue

        matcher = identifierPattern.match(text[current:])
        if matcher:
            identifier = matcher.group()
            keywords = [
                "let", "in", "fn", "where", "aug", "or", "not", "gr", "ge", "ls",
                "le", "eq", "ne", "true", "false", "nil", "dummy", "within", "and", "rec"
            ]
            if identifier in keywords:
                matches.append(("KEYWORD",identifier))
            else:
                matches.append(("IDENTIFIER", identifier))
            current += len(identifier)
            continue

        matcher = integerPattern.match(text[current:])
        if matcher:
            integer = matcher.group()
            matches.append(("INTEGER", integer))
            current += len(integer)
            continue

       

        matcher = operatorPattern.match(text[current:])
        if matcher:
            operator = matcher.group()
            matches.append(("OPERATOR", operator))
            current += len(operator)
            continue

        matcher = stringPattern.match(text[current:])
        if matcher:
            string = matcher.group()
            matches.append(("STRING", string))
            current += len(string)
            continue

        if text[current] in "(),;":
            matches.append(("PUNCTUATION", text[current]))
            current += 1
            continue

        
        print("Error in tokenizing")
        break


for i in matches:
    print(i)








    
