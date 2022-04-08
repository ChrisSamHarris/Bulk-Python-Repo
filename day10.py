# ============================ Challenge 1: Leap Year - Nuumber of Days Function ============================
def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if month > 12 or month < 1:
        return "Invalid input."
    if is_leap(year) == True and month == 2:
        leap_year_feb = month_days[1] + 1
        return leap_year_feb
    return month_days[month - 1]

#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

# ============================ Challenge 2:  ============================

# ============================ Challenge 3:  ============================

# ============================ Challenge 4:  ============================

# ============================ Challenge 5:  ============================

# ============================ Day X Lecture Notes:  ============================