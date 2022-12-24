numbers = (0, 1, 2, 3, 4, 5)


# print(numbers, sep=";")
# print(*numbers, sep=";")

def test_start(*args):
    print(args)
    for x in args:
        print(x)


test_start(0, 1, 2, 3, 4, 5)
