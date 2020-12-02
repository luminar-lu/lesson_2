list_2 = list(input("Введите строчку: "))
index_1 = 0
for a in range(len(list_2) // 2):
    result_1 = list_2[index_1]
    list_2.pop(index_1)
    index_1 = index_1 + 1
    list_2.insert(index_1,result_1)
    index_1 = index_1 + 1
print(list_2)