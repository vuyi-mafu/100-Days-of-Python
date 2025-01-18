def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap_year = True
                return leap_year
                # print("Leap year.")
            else:
                leap_year = False
                return leap_year
                # print("Not leap year.")
        else:
            leap_year = True
            return leap_year
        #   print("Leap year.")
    else:
        leap_year = False
        return leap_year
        # print("Not leap year.")


def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if is_leap(year):
        return 29

    chosen_month = month_days[month - 1]
    return chosen_month


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
