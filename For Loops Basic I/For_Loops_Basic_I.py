#Basic Loop
for x in range(150):
    print(x)

    # Multiples Of Five
for x in range(5, 1000, 5):
    print(x)

    #Counting, the Dojo Way
for x in range(0, 100):
    if x % 5 == 2:
        print('coding')
    if x % 10 == 2:
        print('coding dojo')
    print(x)

    #Whoa. That Sucker's Huge
oddtotal = 0

for number in range(500000+1):
    if(number % 2 != 0):
        oddtotal = oddtotal + number

print(oddtotal)

# Countdown by Fours
for x in range(2018, 0, -4):
    print(x)


    # Flexible Counter
lowNum = 0
highNum = 50
multi = 5

for x in range(lowNum, highNum+1, multi):
    print(x)
