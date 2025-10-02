"""Code to write 3 different versions of code to generate a random Boolean (True or False)."""

# 1
import random

def random_bool_choice():
    return random.choice([True, False])

print(random_bool_choice())

# 2
import random

def random_bool_randint():
    return bool(random.randint(0, 1))

print(random_bool_randint())

# 3
import random

def random_bool_getrandbits():
    return bool(random.getrandbits(1))

print(random_bool_getrandbits())
