import random
print('Welcome to the Numbers Game!')
print('Please enter a number between 1 and 100')
def is_valid(num):
    if num.isdigit() and 1 <= int(num) <= 100:
        return True
    else:
        return False

start = 'y'
while start == 'y':
    n = random.randint(1, 100)
    while True:
        user = input()
        if is_valid(user) == True:
            user = int(user)
            if user > n:
                print('Your number is greater than the guessed one')
            if user < n:
                print('Your number is less than the guessed one')
            if user == n:
                print('You win!')
                break
        else:
            print('Please enter an integer from 1 to 100')
    start = input('Again? (y or n):')