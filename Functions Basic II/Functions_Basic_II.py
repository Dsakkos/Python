# CountDown
from cgi import print_arguments
from multiprocessing import Value


def count(b):
    for x in range(b, -1, -1):
        print(x)
    
    return(x)

x = (count(5))

# Print and Return
def list(a, b):
    print (a)
    x = a + b

    return(x)

x = (list(2,3))

print(x)

# First Plus Length
def first_plus_length(b):
    x = (b[0] + len(b))
    return(x)

x = (first_plus_length([2,3,4,5,6,7,8,9,10]))

print(x)


# Values Greater than Second
def greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output


print(greater_than_second([5,2,3,2,1,4]))
print(greater_than_second([3]))


# This Length, That Value
def length_and_value(num1, num2):
    output = []
    for i in range(0, num1):
        output.append(num2)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
