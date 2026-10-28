import random, string
n = 100  # length
result = ''.join(random.choices(string.ascii_letters + string.digits, k=n))
print(result)