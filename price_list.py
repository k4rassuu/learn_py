#Price_list ^ sgushchenka
#Coded by Vladislav M.
from copy import deepcopy
price_list =[12, 14.6, 55.9, 124.2, 180, 246, 34.2, 442, 94.6, 73.5, 86, 94]

fixed_pl = ""

for i in price_list:
    fixed_pl += f' {int(i // 1)} руб {int(100 * round((i % 1),2))} коп,'

print(fixed_pl)


price_list.sort()
print(f" \n id price_list = {id(price_list)} \n sorted list {price_list} \n and his id = {id(price_list)}")


new_price_list = deepcopy(price_list)

new_price_list.sort(reverse=True)

print(f" \n id new_price_list = {id(new_price_list)} \n new sorted list : {new_price_list} \n id new_price_list == price_list ? - {new_price_list == price_list}")

_=new_price_list[:5]
print(f"\n the 5 top price - {_}")