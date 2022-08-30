# 1. print all integers from 0 to 250
for i in range(251):
    print(i)

# 2. print all the multiples of 5 from 5 to 1000
for i in range(5, 1001, 5):
    print(i)

# 3. print integers 1 to 100, if divisible by 5, print 'Coding' instead, if divisible by 10, print 'Coding Dojo'
for i in range(1, 101):
    if i % 10 == 0:
        print('Coding Dojo')
    elif i % 5 == 0:
        print('Coding')
    else:
        print(i)

# 4. add odd integers from 0 to 500k and print final sum
sum = 0
for i in range(1, 500001, 2):
    sum += i
print(sum)

# 5. print positive numbers from 2018, counting down by 4s
for i in range(2018, 0, -4):
    print(i)

# 6. 3 vars: lowNum, highNum, mult. From lowNum to highNum, print multiple of mult
def flexible_counter(lowNum, highNum, mult):
    for i in range(lowNum, highNum + 1):
        if i % mult == 0:
            print(i)

flexible_counter(2, 9, 3)
