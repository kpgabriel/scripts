ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
result = []
for i in set(ar):
    result.append(ar.count(i) // 2)

print(sum(result))