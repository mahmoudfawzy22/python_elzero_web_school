def show_skills(name, *skills):

    print(f"Hello {name} your skills is: ")

    for skill in skills:
        print(f'''"- {skill}"''')
        
show_skills("Osama", "HTML", "CSS", "JS", "Python")
