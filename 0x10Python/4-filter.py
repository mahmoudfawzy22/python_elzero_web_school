def is_string(element):

    return str(element).isalpha()

skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")

names = list(filter(is_string, skills))

names.reverse()
reversed_skills = skills[::-1]

print(type(skills))

for name in names:

    print(f"{reversed_skills.index(name) + 50} - {name}")
