# Time Convertor
# Coded by Martynov V.

seconds = int(input("Введи число секунд : "))
mins = int(seconds // 60)
hours = int(seconds // 3600)
_seconds = int(seconds % 60)
print(f" {seconds} секунд - это : \n {hours} часов \n {mins - (hours*60)} минут \n {_seconds} секунд.")


