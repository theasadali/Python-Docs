x = str(input("input string: "))

if len(x) <= 10:
    print(x)
elif len(x) > 10:
    print(x[:10])

