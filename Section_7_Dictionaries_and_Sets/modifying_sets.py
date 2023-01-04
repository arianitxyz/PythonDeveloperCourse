# horrible way to declare a set
# numbers = {*""}

# another way to declare a set
# numbers = {*{}}


# numbers = set()
# print(numbers, type(numbers))
# # numbers.add(1)
# # print(numbers)
#
# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value:"))
#     numbers.add(next_value)
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# create a set from the list to record the unique colors

unique_colors = sorted(set(data))
print(unique_colors)

# create a list of unique colors, keeping the order they appeared
unique_colors = list(dict.fromkeys(data))
print(unique_colors)

print()
print(dict.fromkeys(data))
