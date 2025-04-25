#2022-11-04 Quiz 021
#Build a function that produces the truth tabel for 3 inputs and add a column for the boolean equation : AB+(not B)+(notB C)

def table_of_truth_equation():
    print(f"|  A  |  B  |  C  | AB + not B + not CB |")
    for i in range(8):
        a = i//4
        b = (i%4)//2
        c = i%2
        d = int(a and b) or int(not b) or int(not b and c)
        print(f"|  {a}  |  {b}  |  {c}  |          {d}          |")

table_of_truth_equation()