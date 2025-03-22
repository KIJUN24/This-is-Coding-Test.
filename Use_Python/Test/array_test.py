player = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

# print(player.pop(4))
# print(player)
# print(player.append("mine"))
# print(player)

count = 0
for i in range(len(player)):
    for j in range(len(callings)):
        if player[i] == callings[j]:
            count += 1

print(count)

