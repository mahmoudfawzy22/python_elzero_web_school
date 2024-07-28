country = input("Input Your Country").strip().capitalize()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30

if country in countries:
    print(f"Your country Eligile For Discount And The price after Discount Is ${price - discount}")

else:
    print(f"Your country not Eligile for Discount And The price Is {price}")
