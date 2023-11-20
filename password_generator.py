from random import randint

def generate_password(length=64):
    return "".join([chr(randint(33, 126)) for _ in range(length)])