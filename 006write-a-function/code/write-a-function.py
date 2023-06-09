def is_leap(year):
    # the first if statement checks if the year is evenly divisible by 4. If it isn't it will return False. If it is, it moves on to the next line.
    # the first elif statement checks if the year is evenly divisible by 100. If it isn't it will return True. If it is, it moves on to the next line.
    # the next elif statement checks if the year is evely divisible by 400. If it isn't, it returns False. If it is, it moves on to the next line.
    # the last line says that if it doesn't satisfy any of the listed conditions, it IS a leap year.
   
    if (year % 4 != 0):
        return False
    elif (year % 100 != 0):
        return True
    elif (year % 400 != 0):
        return False
    else:
        return True

year = int(input());
print(is_leap(year));
