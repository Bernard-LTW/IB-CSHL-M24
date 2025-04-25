def cut_cake(cake:list,num:int):
    length = len(cake)*len(cake[0])
    if num > length:
        cake = "No cake"
    else:
        a = length//num
        temp=[]
        for i in range(num):
            for j in range(a):
                temp.append(i+1)
        while not len(temp) == length:
            temp.append(0)
        z=0
        for i in range(len(cake)):
            for j in range(len(cake[0])):
                cake[i][j] = temp[z]
                z+=1
    return cake


cake = [[1,2,3],[4,5,6],[7,8,9]]
print(cut_cake(cake, 5))