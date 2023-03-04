import datetime
from dateutil.relativedelta import relativedelta

# prompt the user to enter their birthdate
birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")

# parse the birthdate string into a datetime.date object
birthdate = datetime.datetime.strptime(birthdate_str, '%Y-%m-%d').date()

today = datetime.date.today()

# calculate the age using relativedelta
age = relativedelta(today, birthdate)

# print the age in years, months, and days
print(f"You are {age.years} years, {age.months} months, and {age.days} days old.")
