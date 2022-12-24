# For this exercise, you'll write a function that returns the appropriate response, in the game of fizz buzz.
# It's a simple game, usually played with 2 or more people.
# You start counting, in turn. That's easy enough, but there's a complication.
# If the number is divisible by 3, you say "fizz" instead.
# If it's divisible by 5, you say "buzz".
# And if it's divisible by both 3 and 5, you say "fizz buzz".
# The function must be called fizz_buzz
#   Your fizz_buzz function should return the correct word ("fizz", "buzz" or "fizz buzz"), or the number if it's not
#   divisible by either 3 or 5.
#   The function will always return a string. When you return the number, therefore, you should convert it to a
#   string first.

def fizz_buzz(number: int) -> str:
    """
    Play the game fizz buzz.
    It's a simple game, usually played with 2 or more people.
    You start counting, in turn. That's easy enough, but there's a complication.
    If the number is divisible by 3, you say "fizz" instead.
    If it's divisible by 5, you say "buzz".
    And if it's divisible by both 3 and 5, you say "fizz buzz".
    :param: number: The given number if it ist not divisible by 3,5 or 15
    :return: The answer to the game (fizz, buzz, fizz buzz or the number)
    """
    user_input = int(number)
    if user_input % 3 == 0:
        result = "fizz"
    elif user_input % 5 == 0:
        result = "buzz"
    elif user_input % 15 == 0:
        result = "fizz buzz"
    else:
        result = str(user_input)
    return result


input("Play fizz buzz. Press ENTER to start")
print()

next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go:")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {0}".format(correct_answer))
        break
else:
    print("Well done, you reached {0}".format(next_number))
