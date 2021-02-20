some_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
true_list = []

for i in some_list:
    if i.replace("+","").isdigit():
        if i[0] == "+":
            true_list.append(f'"{i[0] + "0" + i[1:]}"')
        else:
            true_list.append(f'"0{i}"')
    else:
        true_list.append(i)

print(" ".join(true_list))