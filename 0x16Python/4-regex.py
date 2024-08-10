import re 

test = re.finditer(r"(https?):\/\/(www.)?\w+\.(com|org)(:\d+)?\/\w+\.(py|php)", """http://www.elzero.org:8888/link.php
https://elzero.org:8888/link.php
http://www.elzero.com/link.py
https://elzero.com/link.py
http://www.elzero.net
https://elzero.net""")

for group in test :
    print(group)