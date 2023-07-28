import random, string
SECRET_KEY = "".join([random.choice(string.printable) for _ in range(24)])