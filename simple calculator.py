print('\n                       --- CALCULATOR ---\n')

print('LEGEND:\n')
print('+ : addition')
print('- : subtraction')
print('* : multiplication')
print('/ : division')
print('pow : exponentiation')
print('sqrt : square root --- note: input the first operand only')
print('root : nth root')
print('\nExamples:\nType 2*4 and then press <Enter>\nType 4sqrt and then press <Enter>\nType 4root2 and then press <Enter>')

while True:
    x=input('\n')
    x=x.lower()
    if x=='exit':
        break
    elif x=='quit':
        quit()
    if '+' in x:
        s=x.index('+')
        x1=x[:s]
        x2=x[s+1:]
        try:
            x1=float(x1)
            x2=float(x2)
            xop=x1+x2
            print(round(xop,3))
        except ValueError:
            print('\n\nInvalid input\n\nEnter numbers\nnot alphabetical characters')
    if '*' in x:
        s=x.index('*')
        x1=x[:s]
        x2=x[s+1:]
        try:
            x1=float(x1)
            x2=float(x2)
            xop=x1*x2
            print(round(xop,3))
        except ValueError:
            print('\n\nInvalid input\n\nEnter numbers\nnot alphabetical characters')
    if '-' in x:
        s=x.index('-')
        x1=x[:s]
        x2=x[s+1:]
        try:
            x1=float(x1)
            x2=float(x2)
            xop=x1-x2
            print(round(xop,3))
        except ValueError:
            print('\n\nInvalid input\n\nEnter numbers\nnot alphabetical characters')
    if '/' in x:
        s=x.index('/')
        x1=x[:s]
        x2=x[s+1:]
        try:
            x1=float(x1)
            x2=float(x2)
            xop=x1/x2
            print(round(xop,3))
        except ValueError:
            print('\n\nInvalid input\n\nEnter numbers\nnot alphabetical characters')
    if 'pow' in x:
        s=x.index('pow')
        x1=x[:s]
        x2=x[s+3:]
        try:
            x1=float(x1)
            x2=float(x2)
            xop=x1**x2
            print(round(xop,3))
        except ValueError:
            print('\n\nInvalid input\n\nEnter numbers\nnot alphabetical characters')
        except OverflowError:
            print('\nNot enough memory for this operation\nPlease input smaller numbers')
    if 'sqrt' in x:
        s=x.index('sqrt')
        x1=x[:s]
        try:
            x1=float(x1)
            xop=x1**(1/2)
            print(round(xop,3))
        except ValueError:
            print('\n\nInvalid input\n\nEnter numbers\nnot alphabetical characters')
    if 'root' in x:
        s=x.index('root')
        x1=x[:s]
        x2=x[s+4:]
        try:
            x1=float(x1)
            x2=float(x2)
            xop=x1**(1/x2)
            print(round(xop,3))
        except ValueError:
            print('\n\nInvalid input\n\nEnter numbers\nnot alphabetical characters')
        
    
