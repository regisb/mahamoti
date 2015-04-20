import os
import string
import random

def secret_key():
    secret_key_dir = os.path.expanduser("~/.config/mahamoti")
    secret_key_path = os.path.join(secret_key_dir, "secret_key")
    if not os.path.exists(secret_key_dir):
        os.makedirs(secret_key_dir)
    if not os.path.exists(secret_key_path):
        with open(secret_key_path, "w") as f:
            f.write("".join([random.choice(string.letters) for _ in range(0, 50)]))
    return open(secret_key_path).read()
