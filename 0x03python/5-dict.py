languageOne = {
    "name" : "HTML",
    "progress" : "90%"
}

languageTwo = {
    "name" : "CSS",
    "progress" : "80%"
}

languageThree = {
    "name" : "Python",
    "progress" : "30%"
}

languageFour = {
    "name" : "AI",
    "progress" : "20%"
}

total_languages = {
    "HTML" : languageOne,
    "CSS" : languageTwo,
    "Python" : languageThree,
    "AI" : languageFour
}

# print HTML and his progress
print(total_languages["HTML"]["name"] + " progress Is : {}".format(total_languages["HTML"]["progress"]))
# print CSS and his progress
print(total_languages["CSS"]["name"] + " progress Is : {}".format(total_languages["CSS"]["progress"]))
# print Python and his progress
print(total_languages["Python"]["name"] + " progress Is : {}".format(total_languages["Python"]["progress"]))
# print AI and his progress
print(total_languages["AI"]["name"] + " progress Is : {}".format(total_languages["AI"]["progress"]))


