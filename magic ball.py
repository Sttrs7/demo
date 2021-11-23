import random
answers = ['Indisputably', 'Foregone conclusion', 'Without any doubts', 'Highly doubtful', 'Do not even think',
           'try again', 'Better not to tell', 'The signs say yes', 'Most likely']

def ran(name):
    start = 'y'
    while start == 'y':
        print('Hi,', name)
        print('Ask your question')
        input()
        print(random.choice(answers))
        start = input('Do you want to know anything else? (y or n)')
    if start == 'n':
        print('Bye!')



print('Hi, I am a magic ball, what do you want to know?')
print('What is your name?')
ran(input())