import string
import random
upp_str = [i for i in string.ascii_uppercase]
low_str = [j for j in string.ascii_lowercase]
num = [str(n) for n in range(10)]
symbols = [k for k in '{}()[].,:;+-*/&|<>=~']
a = upp_str+low_str+num+symbols

password = []
gen = 0
while gen!='stop':
    gen = input("Do you want to generate random password?")
    if gen == 'yes':
        pwd = ''.join(random.sample(a, 8))
        print(pwd)
        password.append(pwd)
    else:
        break
