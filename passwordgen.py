try:
    import random
    import time
    import sys
    import pyperclip as pc
    import os.path
    import os
except:
    print("Missing modules, Please download required modules.")

# This changes the terminal size.
try:
    cmd = 'mode 75,10'
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
symbol = "!@#$%^&*()_+"

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
email = input("Email for your account: ")
password = "".join(random.sample(all, length))

# This asks for a website that you wanna store email:pass to it.
print("Please enter 2 letters of the website.")
website = input("Website: ")

# This copies the generated password and saves your data in the website you want in a plain text.
print("Your password is copied to clipbaord" + f" And saved your data in {website}.txt")
pc.copy(password)

filepath = os.path.join('./Saved Passwords', f'{website}.txt')
if not os.path.exists('./Saved Passwords'):
    os.makedirs('./Saved Passwords')
f = open(filepath, "a")
f.write(email + " : " + password + '\n')

# End.
time.sleep(3)