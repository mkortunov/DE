# Week_2
def cards(lower_limit, upper_limit):
    x = [i for i in range(lower_limit, upper_limit)]
    y = x
    pairs =[]
    for i in x:
        for j in y:
            if (i+j != 100 and i!=j):
                pairs += [[i,j]]
            else:
                continue
    return pairs

print(len(cards(10,100)))


for x in range(3, 100):
    if (x % 3 == 2 and x % 4 == 3 and x % 5 == 4):
        print(x)