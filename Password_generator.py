import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_.'
chars = ''

howmuch = int(input('How many passwords do you need?'))
ler = int(input('Specify the length of one password'))
digOn = input('Should the digits 0123456789 be included? (y/n)')
ABCon = input('Should the uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ be included? (y/n)')
abcOn = input('Should the lowercase letters abcdefghijklmnopqrstuvwxyz be included? (y/n)')
chOn = input('Should the symbols !#$%&*+-=?@^_ be included? (y/n)')
excOn = input('Exclude il1Lo0O ambiguous characters? (y/n)')

if digOn == 'y':
    chars += digits
if ABCon == 'y':
    chars += uppercase_letters
if abcOn == 'y':
    chars += lowercase_letters
if chOn == 'y':
    chars += punctuation
if excOn == 'y':
    for k in 'il1Lo0O':
        chars = chars.replace(k, '')

def generate_password(lenght, chars):
    passs = ''
    for i in range(lenght):
        passs += random.choice(chars)
    print(passs)

for j in range(howmuch):
    generate_password(ler, chars)