from random import randint

def generate_password(length):
    return "".join([chr(randint(33, 126)) for _ in range(length)])