#2022-11-29 Quiz 029

#Create a function that receives a dictionary with letters in the alphabet as keys and a string. The functions returns the dictionary with a count as value for the occurrence of each letter:

dict = {'w':0, 'l':0,'c':0}
dict2 = {'a':0, 'e':0,'i':0, 'o':0, 'u':0}

def count_letters(my_dict, string):
    for i in string:
        if i in my_dict:
            my_dict[i] += 1
    return my_dict

print(count_letters(dict, "hello world"))

print(count_letters(dict2, "Why did I choose CS?"))

