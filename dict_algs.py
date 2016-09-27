ivan = {
    "name" : "ivan",
    "age" : 3,
    "children" : [{
        "name" : "vasja",
        "age" : 12,
    }, {
        "name" : "petja",
        "age" : 10,
    }],
}

darja = {
    "name": "darja",
    "age" : 41,
    "children" : [{
        "name" : "kirill",
        "age" : 21,
    }, {
        "name" : "pavel",
        "age" : 15,
    }],
}
emps = [ivan, darja]

def older18(masdic):
    mas = []
    for dic in masdic:
        for child in dic['children']:
            if child['age'] > 18:
                mas.append(dic['name'])
                break
    return mas

print(older18(emps))