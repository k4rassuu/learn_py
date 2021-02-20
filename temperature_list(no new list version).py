some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, n in enumerate(some_list):
    if n.replace("+", "").isdigit():
        if n[0] == "+":
            some_list[i] = f'"{n[0]}0{n[1:]}"'
        else:
            some_list[i] = f'"0{n}"'
print(" ".join(some_list))