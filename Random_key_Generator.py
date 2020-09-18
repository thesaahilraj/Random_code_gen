import random
from colorama import init, Fore
import string
import os

init(convert=True)


def gen(fix, amount):
    while fix <= amount:
        code = ('').join(random.choices(
            string.ascii_letters.upper() + string.digits.upper(), k=4))
        code2 = ('').join(random.choices(
            string.ascii_letters.upper() + string.digits.upper(), k=4))
        code3 = ('').join(random.choices(
            string.ascii_letters.upper() + string.digits.upper(), k=4))
        f.write(code.upper() + "-" + code2.upper() +
                "-" + code3.upper() + '\n')
        print(code.upper() + "-" + code2.upper() + "-" + code3.upper())
        fix += 1


print(Fore.BLUE + Fore.WHITE)
f = open('keys.txt', 'a')
print(Fore.BLUE + 'Enter the number of codes to be generated: ')
amount = int(input())
fix = 1
gen(fix, amount)
