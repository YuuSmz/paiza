import os

a, b = input().split()
path = os.path.join(a, b)
print(os.path.realpath(path))
