#Bubble Sort Algorithm

array1 = [5, 3, 8, 6, 7, 2]

def bubbleSort(x):
    count = 0
    for i in range(len(x)):
        for j in range(len(x)-1):
            if x[j] > x[j+1]:
                count += 1
                x[j], x[j+1] = x[j+1], x[j]
    return x, count

result, count = bubbleSort(array1)

print(f"Sorted array: {result}")
print(f"Number of swaps: {count}")