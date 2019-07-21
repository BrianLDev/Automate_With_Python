

def collatz(number):
    if number % 2 == 0:
        number = number // 2
    else:
        number = 3 * number + 1
    print(number)
    return number

# Get a number from the user and keep running collatz until a 1 is returned
userNum = None
while(userNum == None):
    try:
        print("Enter a number: ")
        userNum = int(input())
    except ValueError: 
        print("***   Only numbers!!   ***")

while(userNum != 1):
    userNum = collatz(userNum)

