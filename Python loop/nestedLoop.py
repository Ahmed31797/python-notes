name = "Ali"
name2 = "Nur"
for l in name:
    for l2 in name2:
        print(l, l2)


numbers = [1,2,3,5,6,7,8,9,10]
numbers2 = [1,2,3,5,6,7,8,9,10]
for n1 in numbers:
    for n2 in numbers2:
        print(n1 * n2)



abdiFriends = ["Ali", "Ahmed", "Yussuf", "Aden", "Qasim"]
aliFriends = ["Ducaal", "Shaalle", "Yussuf", "Aden", "Qasim"]
for f in abdiFriends:
    for f2 in aliFriends:
        if f == f2:
            print (f2)