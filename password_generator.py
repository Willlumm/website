from random import choices

def generate_password(chars, length):
    return "".join(choices(chars, k=length))