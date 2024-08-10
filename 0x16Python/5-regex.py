import re

text = """
http
https
abcd
abcd
"""

# pattern = r"http|https"
# matches = re.findall(pattern, text)
# print(matches)

# pattern = r"(https?)"
# matches = re.findall(pattern, text)
# print(matches)

# pattern = r"(h\w{3})\w?"
# matches = re.findall(pattern, text)
# print(matches)

# pattern = r"(\wtt)(\w{1,2})"
# matches = re.finditer(pattern, text)

# for group in matches:
#     print(group)

pattern = r"^https?$"
matches = re.findall(pattern, text, re.MULTILINE)
print(matches)
