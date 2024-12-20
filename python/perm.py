def perm(l):
    if len(l) <= 1:
        return [l]
    r = []
    for i in range(len(l)):
        s = l[:i] + l[i+1:]
        p = perm(s)
        for x in p:
            r.append(l[i:i+1] + x)
    return r

result = perm(['a', 'b', 'c', 'd', 'e', 'f'])

with open("permutations.txt", "w") as file:
    file.write("All permutations:\n")
    for perm in result:
        file.write(str(perm) + "\n")

print("Permutations written to 'permutations.txt'")
