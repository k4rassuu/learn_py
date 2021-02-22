def thesaurus(*args):
    name_dict = {}
    for name in args:
        if name[0] in name_dict.keys():
            name_dict[name[0]].append(name)
        else:
            name_dict[name[0]] = [name]
    print(name_dict)
    return
thesaurus("Петр", "Оксана", "Лена", "Ульяна", "Чадомир", "Илья", "Ꮑеонид", "0лег", "Светлана", "Ь")

