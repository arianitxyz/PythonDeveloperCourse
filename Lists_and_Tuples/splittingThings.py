panagram = "The quick brown fox jumps over the wall"

print(panagram.split())

numbers = "9,223,432,785,123,123"
numbers_list = (numbers.split(","))

#values = "".join(char if char not in separators else " " for chat in numbers).split()

generated_list = ['9', '',
                  '2', '7', '3', '',
                  '1', '6', ''
                  ]

values = "".join(generated_list)
values_list = values.split()
print(values_list)


for index in range(len(numbers_list)):
    numbers_list[index] = int(numbers_list[index])
print(numbers_list)