from datetime import datetime

today_is = datetime(2021, 8, 10)

# 2021-08-10
print(today_is.strftime("%Y-%m-%d"))

# Aug 10, 2021
print(today_is.strftime("%b %d, %Y"))

# 10 - Aug - 2021
print(today_is.strftime("%d - %b - %Y"))


# 10 / Aug / 21
print(today_is.strftime("%d / %b / %y"))

# 10 / August / 2021
print(today_is.strftime("%d / %B / %Y"))

# Tue, 10 August 2021
print(today_is.strftime("%a, %d %B %Y"))
