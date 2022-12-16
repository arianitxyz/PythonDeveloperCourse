print("Enter three numbers to be added nut separated by a comma ,")

numbers = input()

numbers_list = numbers.split(",")
print(numbers_list)

for i in  range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)


a, b, c = numbers_list
result = a + b - c
print(result)

#
print(int(numbers_list[0]) + int(numbers_list[1]) - int(numbers_list[2]))
