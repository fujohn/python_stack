# 1. countdown: accepts a number, return list that counts down by 1 from number to 0
def countdown(num):
    return list(range(num, -1, -1))

print(countdown(5))

# 2. print & return: receive list with 2 nums, print first value and return second
def print_and_return(lst):
    if len(lst) != 2:
        return None
    print(lst[0])
    return lst[1]

print(print_and_return([1,2]))

# 3. first + length: accepts list and returns sum of first val plus list of length
def first_plus_length(lst):
    return lst[0] + len(lst)

print(first_plus_length([1,2,3,4,5]))


# 4. values > than second: accepts list and creates new list containing only values of list > second value. 
# Print how many values this is and return new list. If list < 2 elements, return false
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    else:
        new_lst = []
        for i in lst:
            if i > lst[1]:
                new_lst.append(i)
        print(len(new_lst))
        return new_lst

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

# 5. This length, that value: accepts 2 ints: size and value. create and return list whose length = given size & values are all the given value
def length_and_value(size, value):
    return [value] * size

print(length_and_value(4,7))
print(length_and_value(6,2))