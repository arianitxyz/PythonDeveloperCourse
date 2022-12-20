
def isPalindromeSentence(string):
    newString = ""
    for char in string:
        if char.isalnum():
            newString += char
    print(newString)
    #return newString.casefold() == newString[::-1].casefold()
    return

sentence = input("Please input a sentence \n")

if isPalindromeSentence(sentence):
    print(print("It is a palindrome"))
else:
    print("{} is not a palindrome".format(sentence))