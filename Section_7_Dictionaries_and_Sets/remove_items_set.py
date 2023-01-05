small_ints = set(range(21))
print(small_ints)
# small_ints.clear()
# print(small_ints)

small_ints.discard(10)
small_ints.remove(11)
print(small_ints)

small_ints.discard(99)

# remove causes a crash if the item does not exist
# small_ints.remove(99)
