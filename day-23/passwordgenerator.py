import random

char="!@#$%^&*()qwertyuioplkjhgfdsazxcvbnm[{}]|\:<>?123654789/*-+"
passlen=8
p = "".join(random.sample(char,passlen))
print(p)
