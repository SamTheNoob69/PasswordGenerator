import random
import time
import sys
import os.path
import os
import subprocess
import sys

try:
    import pyperclip as pc
except ImportError:
    print("Missing PyperClip Module, Downloading will begin soon...")
    time.sleep(3)
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyperclip'])
finally:
    import pyperclip as pc

try:
    from termcolor import colored, cprint
except ImportError:
    print("Missing TermColor Module, Downloading will begin soon...")
    time.sleep(3)
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'termcolor'])
finally:
    from termcolor import colored, cprint

# This changes the terminal size.
try:
    cmd = 'mode 100,10'
    os.system(cmd)
except:
    pass

# This changes the terminal color.
try:
    cmd2 = 'color a'     
    os.system(cmd2)
except:
    pass

# Letters and Numbers And Symbols to include in password.
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
symbol = "!@#$%^&*()"

all = lower + upper + num + symbol

# This will read the number in the default location for the length of the password.
file = open("default.length.txt", 'r')
length = int(file.readline().strip())
file.close()


# Additional feature.
"""
try:
    length = int(input("Length of password you want to generate: "))
except:
    print("This is not a number!")
    time.sleep(3)
    sys.exit()
if length < 8 or length > 32:
    print("Your length must be longer than '8' | And must not be longer than '32'")
    time.sleep(3)
    sys.exit()
else:
    pass
"""

# This asks for some information.
while True:
    email = input("Email for your account: ")
    if not "@" in email:
        print(f"({email}): is not a real email.")
    elif not "." in email:
        print(f"({email}): is not a real email.")
    else:
        break
password = "".join(random.sample(all, length))

# This asks for a website that you wanna store email:pass to it.
print("Please enter 2 letters of the website.")
while True:
    website = input("Website: ")
    if len(website) != 2:
        print(f"({website}): is not 2 letters.")
    else:
        break


# This copies the generated password and saves your data in the website you want in a plain text.
import pathlib
currentpath = pathlib.Path(__file__).parent.resolve()


print("Your password is copied to clipbaord," + f" And saved your data in:")
cprint(f'{currentpath}\Saved Passwords\{website}.txt"', 'red')
pc.copy(password)


filepath = os.path.join('./Saved Passwords', f'{website}.txt')
if not os.path.exists('./Saved Passwords'):
    os.makedirs('./Saved Passwords')
f = open(filepath, "a")
f.write(email + " : " + password + '\n')

# End.
time.sleep(5)
