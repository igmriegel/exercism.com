def leap_year(year):
    mod_4 = year % 4 == 0
    mod_100 = year % 100 == 0
    mod_400 = year % 400 == 0

    if mod_100 and not mod_400:
        return False
    
    if mod_4 or (mod_4 and mod_400):
        return True

    return False