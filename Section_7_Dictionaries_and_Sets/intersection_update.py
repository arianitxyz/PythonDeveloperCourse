# Your task for this coding exercise is to find out which prepositions have been used in the quote:
#
# "Education is not the learning of facts but the training of the mind to think – Albert Einstein"
#
# There are two steps you'll need to perform:
#
#     Split text to create a list of words.
#
#     Create an intersection of the set of words with the prepositions set that we've provided in the exercise code.
#
# In order for the on-line checker to validate your solution, it's essential that you use the name preps_used for the intersection that you create.
#
# Please do NOT modify the lines of starter code given to you - write your code in the space indicated.

text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# Add your code here.


words = text.split()

preps_used = set(words) & prepositions
print(preps_used)

# words = text.split()
#
# preps_used = prepositions.intersection(words)
# print(preps_used)
