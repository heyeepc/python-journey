a = [1,2,3,4]

for i in a:
    for j in a:
        for k in a:
            if i != j and i != k and j != k:
                print(f"{i}{j}{k}")

