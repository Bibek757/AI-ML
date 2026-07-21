
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


# 6: Store a student's details in a dictionary and print them
student = {"name": "Alex", "age": 20, "course": "AI/ML"}
print("Name:", student["name"])
print("Age:", student["age"])
print("Course:", student["course"])


# 7: Count how many times each word appears in a list
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)


# 8: Add a new key-value pair to a dictionary and update an existing one
person = {"name": "Sam", "city": "Delhi"}
person["age"] = 22          # add new key
person["city"] = "Mumbai"   # update existing key
print(person)


# 9: Check whether age exists or not 
student = {
    "name":"Bibek",
    "course":"CS"
}

if "age" in student:
    print("Exists")
else:
    print("Not Found")


