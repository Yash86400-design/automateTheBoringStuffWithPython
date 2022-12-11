try:
    value = int(input("Enter number: \n"))
except:
    print("Input must be integer.")


def collatz(number):

    if (number == 1):
        return

    elif (number % 2 == 0):
        print(number//2)
        number = number//2
        return collatz(number)

    else:
        print(3 * number + 1)
        number = 3 * number + 1
        return collatz(number)


collatz(value)
