animals = {'Turtle',
           'Horse',
           'Python',
           'Swallow',
           'Hedgehog',
           'Wren',
           'Ardvark',
           'Cat',
           "Robin",
           }
birds = {'Robin', "Swallow", "Wren", }
garden_birds = {'Robin', "Swallow", "Wren", }

print(f'birds is a substring of animals:{birds.issubset(animals)}')
print(f'animals is a superstring of bird:{animals.issuperset(birds)}')

print(birds == garden_birds)
print(birds <= garden_birds)
