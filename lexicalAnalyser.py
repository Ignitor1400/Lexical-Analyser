import re

f = open('Input.c', 'r')

headers = ['<math.h>', '<stdio.h>', '<string.h>', '<conio.h>']
operators = ['=', '+', '-', '/', '*', '++', '--', '==', '>', '<', '>=', '<=']
keywords = ['int', 'float', 'char', 'long', 'return', 'if', 'else', 'include', 'scanf', 'printf', 'main']
identifiers = ['n1', 'n2', 'n3', 'sum']
literals = ['0', 'is_the_largest_number.', 'Enter_three_different_numbers: ', ]
symbols = ['{', '}', '[', ']', '(', ')', '#', ';', ',', '"']
hc = 0
oc = 0
kc = 0
ic = 0
lc = 0
sc = 0

he = []
op = []
ke = []
ide = []
li = []
sy = []

i = f.read()

count = 0
program = i.split('\n')

for line in program:
    tokens = line.split()
    for token in tokens:
        if token in headers:
            hc += 1
            he.append(token)
        elif token in operators:
            oc += 1
            op.append(token)
        elif token in keywords:
            kc += 1
            ke.append(token)
        elif token in identifiers:
            ic += 1
            ide.append(token)
        elif token in literals:
            lc += 1
            li.append(token)
        elif token in symbols:
            sc += 1
            sy.append(token)
print("Header Count: {}\nHeaders:".format(hc))
print(he)
print("Operator Count: {}\nOperators:".format(oc))
print(op)
print("Keyword Count: {}\nKeywords:".format(kc))
print(ke)
print("Identifier Count: {}\nIdentifiers:".format(ic))
print(ide)
print("Literal Count: {}\nLiterals:".format(lc))
print(li)
print("Special Symbol Count: {}\nSpecial symbols:".format(sc))
print(sy)


'''
for i in he:
    print(i, end=" , ")
print("\n")
print("Operator Count: {}\nOperators:".format(oc))
for i in op:
    print(i, end=" , ")
print("\n")
print("Keyword Count: {}\nKeywords:".format(kc))
for i in ke:
    print(i, end=" , ")
print("\n")
print("Identifier Count: {}\nIdentifiers:".format(ic))
for i in ide:
    print(i, end=" , ")
print("\n")
print("Literal Count: {}\nLiterals:".format(lc))
for i in li:
    print(i, end=" , ")
print("\n")
print("Special Symbol Count: {}\nSpecial symbols:".format(sc))
for i in sy:
    print(i, end=" , ")
print("\n")
'''
f.close()
