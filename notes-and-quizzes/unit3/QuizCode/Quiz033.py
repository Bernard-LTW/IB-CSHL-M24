#2023-01-10 Quiz 033

def mystery(list1, list2:list):
    output = []
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                output.append(list1[i])
    return output

