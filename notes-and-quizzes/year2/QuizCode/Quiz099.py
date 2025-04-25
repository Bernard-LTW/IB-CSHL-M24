def box(input_list:list):
    x = []
    for i in range(len(input_list)):
        num = input_list[i]
        flag = True

        for j in range(len(x)):
            if num == x[j]:
                flag = False
                break
        if flag:
            x.append(num)
    return x

n = box([3,4,5,5,5,7,7,2,1,1])
print(n)