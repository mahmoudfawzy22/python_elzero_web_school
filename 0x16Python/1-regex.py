import re 

test = re.findall(r"\w\s" ,"eeeeE llllLl lllzzZzzzz eroe operationr pollo ")

for group in test :
    print(group, end="")
