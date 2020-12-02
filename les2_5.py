my_list = [7, 5, 3, 3, 2]
num = int(input("Введите цифру: "))
if num > my_list[0]:
    my_list.insert(0,num)
elif num < my_list[len(my_list)-1]:
    my_list.insert((len(my_list)),num)
else:
    a = 0
    while num < my_list[a]:
        a +=1
    my_list.insert(a+1,num)
print(my_list)
