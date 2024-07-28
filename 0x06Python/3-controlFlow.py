age = int(input("what\'s Your Age ?"))

if age > 10 and age < 100:
    print(f"Age in years {age}")

    ageInMonths = age * 12
    print(f"Age in months {ageInMonths}")

    ageInDays = ageInMonths * 30
    print(f"Age in days {ageInDays}")

    ageInHours = ageInDays * 12
    print(f"Age in hours {ageInHours}")

    ageInminutes = ageInHours * 60
    print(f"Age in minutes {ageInminutes}")

    ageInSeconds = ageInminutes * 60
    print(f"Age in seconds {ageInSeconds}")
else:
    print("Your age out of the scale")
