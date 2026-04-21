def month_to_season(month):
    if month in [12, 1, 2]:
        return "Qish"
    elif month in [3, 4, 5]:
        return "Bahor"
    elif month in [6, 7, 8]:
        return "Yoz"
    elif month in [9, 10, 11]:
        return "Kuz"
    
print(month_to_season(1))  # Qish
print(month_to_season(4))  # Bahor
print(month_to_season(7))  # Yoz
print(month_to_season(10)) # Kuz