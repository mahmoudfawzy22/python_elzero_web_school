LETTER = input("Add Letter From A to Z").strip()

try:
    if len(LETTER) != 1 :
        raise IndexError
    elif not LETTER.isupper() :
        raise ValueError
    
except IndexError :
    print("You Must Write One Character Only")

except ValueError:
    print("The Letter Not In A - Z")

else :
    print("You Typed ", LETTER)
