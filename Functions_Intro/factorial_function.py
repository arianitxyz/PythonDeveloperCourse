def factorial(number: int) -> int:
    """
    Returns the factorial value of the number that you enter
    :param number: The number whose factorial value this calculates
    :return: factorial value of the entered number
    """
    number = int(number)
    if number <= 1:
        return 1
    result = 2
    for i in range(3, number + 1):
        result *= i
    return result


for i in range(36):
    print(i, factorial(i))
