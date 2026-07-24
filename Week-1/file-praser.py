

def create_sample_file():
    with open("scores.txt", "w") as f:
        f.write("Alex,85\n")
        f.write("Sam,92\n")
        f.write("Jordan,78\n")
        f.write("Priya,95\n")
        f.write("Ravi,60\n")
 
 
def parse_file(filename):
    students = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            parts = line.split(",")
            name = parts[0]
            score = int(parts[1])
            students.append({"name": name, "score": score})
    return students
 
 
def print_report(students):
    print("Student Scores")
    for student in students:
        print(student["name"], "-", student["score"])
 
    total = 0
    for student in students:
        total += student["score"]
    average = total / len(students)
    print("\nAverage score:", average)
 
    top_student = students[0]
    for student in students:
        if student["score"] > top_student["score"]:
            top_student = student
    print("Top scorer:", top_student["name"], "-", top_student["score"])
 
 
create_sample_file()
students = parse_file("scores.txt")
print_report(students)