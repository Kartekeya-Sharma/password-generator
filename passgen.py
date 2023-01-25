import random

def passgen(leng):
    l_low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    l_upp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    l_no = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    l_sym = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    temp = []
    
    lowch = input("Lowercase letters?(Y/N): ")
    upch = input("Uppercase letters?(Y/N): ")
    noch = input("Numbers?(Y/N): ")
    l_sym = input("Symbols?(Y/N): ")
    
    if lowch=="Y":
        for i in range(0,leng):
            temp.append(random.choice(l_low))
            temp.append(random.choice(l_upp))
            temp.append(random.choice(l_no))
            temp.append(random.choice(l_sym))
        print(''.join(temp))
    
leng = int(input("Enter length of the password you want: "))
passgen(leng)