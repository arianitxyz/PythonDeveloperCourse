def multiply(x, y):
    result = x * y
    return result


def isPalindrome(string):
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


# word = input("Please enter a word to check if it is a palindrome")
# if isPalindrome(word):
#     print("{}. is a palindrome".format(word))
# else:
#     print("{} is not a palindrome".format(word))


def isPalindromeSentence(string):
    newString = ""
    for char in string:
        if char.isalnum():
            newString += char
    print(newString)
    # return newString.casefold() == newString[::-1].casefold()
    return isPalindrome(newString)


#
#
# sentence = input("Please input a sentence \n")
#
# if isPalindromeSentence(sentence):
#     print(print("It is a palindrome"))
# else:
#     print("{} is not a palindrome".format(sentence))

answer = multiply(18, 3)
print(answer)