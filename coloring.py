L = ["blue", "green", "orange", "grey", "pink"]
c = []
n = 4
v = ["v1", "v2", "v3", "v4"]
E = ["v1", "v2", "v3", "v4"]
def color():

    for i in range(n):
        c.append(L[i])
        for j in range(n):
            if i < j and (v[i], v[j]) in E:
                print("hi")
                for c[i] in L[j]:
                    del c[i]
            print(L[j])
    print(v, n, L, c)
    return v, n, L, c
color()

