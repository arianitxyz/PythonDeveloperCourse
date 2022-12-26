# Your task for this coding exercise is to write some code to count the number of times each character occurs in the
# given `text` string (see the starter code in exercise.py).
#
# You have to do this for every unique character in the given string. Only count characters and digits - don't include
# spaces, punctuation or other symbols.
#
# When counting the characters, ignore case. For example, the string "Be bold" would have a count of 2 for the letter
# 'b'.
#
# Store the count in the `word_count` dictionary that has been declared for you, in the starter code.
#
# The key must be the character, and the value associated with this key should be the count of this particular character
# in the `text`.
#
# For example:
#
# If the `text` was "abcbcc", your `word_count` dictionary will have 3 key value pairs:
#
#
# 'a': 1, 'b': 2 and 'c': 3
#
# (order does not matter).
#
# Please do NOT modify the lines of starter code given to you, write your code in the space indicated.

character_count = {}


def count_characters(text: str):
    for char in text:
        character_count[char] = character_count.setdefault(char, 0) + 1
    print(sorted(character_count.items()))


test = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
       "industry's " \
       "standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to" \
       " make" \
       " a type specimen book. It has survived not only five centuries, but also the leap into electronic " \
       "typesetting, " \
       "remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets " \
       "containing " \
       "Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including " \
       "versions of Lorem Ipsum."

count_characters(test)
