def is_palindrome(number):
    number = "{0:b}".format(number)
    length = len(number)
    result = True

    for i in range(0, int( length / 2)):
        if number[i] != number[ length - i - 1]:
            result = False
            break

    return result 
def odd_number_of_1(number):
    counter = 0
    number = "{0:b}".format(number)
    length = len(number)
    
    for i in range(0, int(length)):
        if number[i] == "1":
            counter += 1

    return (counter % 2 != 0)

def is_hack_number(number):
    return ( is_palindrome(number) and odd_number_of_1(number) )

def next_hack(number):
    number += 1
    while is_hack_number(number) != True:
        number += 1

    return number

print (next_hack(5) )
