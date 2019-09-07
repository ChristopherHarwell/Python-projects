import random, string

# Ranndom Name Generator
#Create 5 random letters for a random 5 letter baby name
# the variable L is the letter and the corresponding number is the number of the letter
L1_Input = input("choose a letter...'v' for vowels, 'c' for consonants, 'l' for any other: ")
L2_Input = input("choose a letter...'v' for vowels, 'c' for consonants, 'l' for any other: ")
L3_Input = input("choose a letter...'v' for vowels, 'c' for consonants, 'l' for any other: ")
L4_Input = input("choose a letter...'v' for vowels, 'c' for consonants, 'l' for any other: ")
L5_Input = input("choose a letter...'v' for vowels, 'c' for consonants, 'l' for any other: ")

# Variable Parameters
vowels = 'aeiouy'
consonants = 'bcdfghjklmnpqrstvwxz'
letter = string.ascii_lowercase


def RGenerator():
    if L1_Input == 'v':
        L1 = random.choice(vowels)
    elif L1_Input == 'c':
        L1 = random.choice(consonants)
    elif L1_Input == 'l':
        L1 = random.choice(letter)
    else:
        L1 = L1_Input # let user choose specific letter

    if L2_Input == 'v':
        L2 = random.choice(vowels)
    elif L2_Input == 'c':
        L2 = random.choice(consonants)
    elif L2_Input == 'l':
        L2 = random.choice(letter)
    else:
        L2 = L2_Input # let user choose specific letter
    
    if L3_Input == 'v':
        L3 = random.choice(vowels)
    elif L3_Input == 'c':
        L3 = random.choice(consonants)
    elif L3_Input == 'l':
        L3 = random.choice(letter)
    else:
        L3 = L_input_3 # let user choose specific letter
    
    if L4_Input == 'v':
        L4 = random.choice(vowels)
    elif L4_Input == 'c':
        L4 = random.choice(consonants)
    elif L4_Input == 'l':
        L4 = random.choice(letter)
    else:
        L4 = L4_Input # let user choose specific letter

    if L5_Input == 'v':
        L5 = random.choice(vowels)
    elif L5_Input == 'c':
        L5 = random.choice(consonants)
    elif L5_Input  == 'l':
        L5 = random.choice(letter)
    else:
        L5 = L5_Input # let user choose specific letter
    Rname = L1 + L2 + L3 + L4 + L5
    return (Rname)
for BabyNames in range(278):
    print(RGenerator())