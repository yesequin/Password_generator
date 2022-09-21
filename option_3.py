
#WE WILL USE SOME COMMON STRING OPERATIONS TO CREATE EACH LIST

import random
import string


def letters():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    characters = lowercase + uppercase + numbers + symbols

    password = []

    for i in range(10):
        random_character = random.choice(characters)
        password.append(random_character)

    password = ''.join(password)
    return password
    


def run():
    password = letters()
    print(f'Your new password is {password}')


if __name__ == '__main__':
    run()


