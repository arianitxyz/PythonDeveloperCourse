import shelve
import random

help(random.randint)

for obj in dir(shelve.Shelf):
    if obj[0] != '_':
        print(obj)

# print(dir())
# print()
# print(dir(shelve))

# test = []
# for m in dir(__builtins__):
#     test.append(m)
#     print(m)
# print('*' * 20)
# print(sorted(test))
