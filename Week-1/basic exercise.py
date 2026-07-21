
# 1: Sum of List
numbers = [10, 20, 30, 40, 50]

total = 0
for num in numbers:
    total += num

print(total)


# 2: Largest Number
numbers = [8, 12, 3, 55, 21]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)


# 3: Even Numbers
numbers = [1,2,3,4,5,6,7,8]

for num in numbers:
    if num % 2 == 0:
        print(num)


# 4: Reverse List
fruits = ["Apple", "Banana", "Orange", "Mango"]

for fruit in reversed(fruits):
    print(fruit)