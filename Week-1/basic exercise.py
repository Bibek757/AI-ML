##### LIST
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




## Dictionaries


# 5: Store a student's details in a dictionary and print them
student = {"name": "Alex", "age": 20, "course": "AI/ML"}
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# 6: Count how many times each word appears in a list
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)


# 7: Add a new key-value pair to a dictionary and update an existing one
person = {"name": "Sam", "city": "Delhi"}
person["age"] = 22          # add new key
person["city"] = "Mumbai"   # update existing key
print(person)


# 8: Check whether age exists or not 
student = {
    "name":"Bibek",
    "course":"CS"
}

if "age" in student:
    print("Exists")
else:
    print("Not Found")



#### LOOP

# 9: Print numbers from 1 to 10 using a loop
for i in range(1, 11):
    print(i)


# 10: print all even numbers from 1 to 20 using a loop
for i in range(1, 21):
    if i % 2==0:
        print(i)


# 11: Print the multiplication table of a given number using a loop
number = 5
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")

# 12: Count down from 10 to 1, then print "finished"
count = 10
while count > 0:
    print(count)
    count -= 1
print("Finished!")


#### FUNCTIONS

# 12: function that checks if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
 
print(is_prime(17))   # True
print(is_prime(15))   # False


# 13: function that returns the factorial of a number
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result = result * i
    return result

print(factorial(5))  # 120



# 14: function that returns the maximum of two numbers
def maximum(a, b):
    if a > b:
        return a
    return b

print(maximum(10, 25))


# 15: function that greets a person
def greet(name):
    print("Hello", name)

greet("Bibek")


# 16: function that calculates the square of a number
def square(n):
    return n * n

print(square(6))


### FILE I/O

# 18: Write a  list of fruits to a text file, one per line
fruits = ["Apple", "Banana", "Cherry", "Date", "Mango"]
with open ("fruits.txt", "w") as f:
    for fruits in fruits:
        f.write(fruits + "\n")



# 19: Read the contents of the text file and print them
with open("fruits.txt", "r") as f:
    contents = f.read()
    print(contents)



# 20: Count the number of lines in a text file
with open("fruits.txt", "r") as f:
    lines = f.readlines()
print("Number of lines:", len(lines))

