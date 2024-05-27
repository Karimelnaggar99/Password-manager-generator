import random
import string


def generate_password():
    letters= string.ascii_letters
    digits= string.digits
    special = string.punctuation
    # print(letters,digits,special)
    min_length=int(input("ENter the minimum length: "))
    numbers =input("Do you want to have numbers?(y/n) ").lower() =='y'
    special_characters = input("Do you want special characters?(y/n)").lower()=='y'

    characters=letters
    if numbers:
        characters+=digits
    if special_characters:
        characters+=special
    pwd=""
    meet_criteria = False
    has_number = False
    has_special =False
    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd+=new_char
        if new_char in digits:
            has_number =True
        elif new_char in special:
            has_special = True
        meet_criteria = True
        if numbers:
            meet_criteria= has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special
    return pwd

