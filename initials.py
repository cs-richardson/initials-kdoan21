fullname = input("Input your full name: ")
initials = ""

name_list = fullname.split()

for name in name_list:
    initials = initials + name[0].upper()

print("Your initials are: ", initials)
