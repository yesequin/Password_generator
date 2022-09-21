#WE WILL USE ASCII CODE TO GENERATE ONE UNIQUE LIST WITH SYMBOLS, NUMBERS, UPPERCASE AND LOWERCASE LETTERS

import random


def all():
    characters =[]
    password = []

    for i in range(33, 127):
        upperCase =chr(i) #chr receives a number and returns its representation as a character.
        characters.append(upperCase)

    for i in range(10):
        random_character= random.choice(characters)
        password.append(random_character)

    password = ''.join(password)
    return password


def run():
    password = all()
    print(f'Your new passowrd is: {password}')


if __name__ == '__main__':
    run()