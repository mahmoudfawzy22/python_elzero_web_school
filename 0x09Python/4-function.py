def say_hello(name='unknown', age='unknown', country='unknown'):
    print(f"Hello {name.strip().capitalize()}. Your age is {str(age).strip()} and your country is {country.strip().capitalize()}.")

# Test
say_hello("Osama", 38, "Egypt")


