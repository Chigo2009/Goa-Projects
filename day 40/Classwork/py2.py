def filter_friends(namess):
    return [name for name in namess if len(name) == 4]
namess_list = ["გიო", "ალექსი", "დემეტრე", "საბა", "დავითი", "ლუკა"]
friends = filter_friends(namess_list)
print(friends)

