#2022-11-01 Quiz 020

#Prompt: Create a function that produces the table of Truth for 3 inputs


def table_of_truth():
    print(f"|  A  |  B  |  C  |")
    for i in range(8):
        a = i//4
        b = (i%4)//2
        c = i%2
        print(f"|  {a}  |  {b}  |  {c}  |")

table_of_truth()