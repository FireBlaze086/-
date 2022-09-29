aggain = 'f'
while aggain == 'f':
    a = float(input("введіть перще число"))
    b = input("введіть знак")
    c = float(input("введіть друге число"))
    if b == '+':
        print(a + c)
    elif b == '-':
        print(a - c)
    elif b == '/':
        if c != 0:      
            print(a / c)
        else:
            print('ділення на 0')
    elif b == '*':
        print(a * c)
    else:
        print("Error")
    aggain = input("введіть 'f' щоб продовжити")
    