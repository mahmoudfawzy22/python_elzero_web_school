from datetime import datetime

old_date = datetime(2021, 6, 25)
new_date = datetime(2021, 8, 10)

old_date_formatted = old_date.strftime("%Y-%m-%d")
new_date_formatted = new_date.strftime("%Y-%m-%d")

print(f"Days form {old_date_formatted} to {new_date_formatted} Is => {(new_date -  old_date).days}")

