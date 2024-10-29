name = input("What is the student's name?: ")

print("\nEnter marks for each subject (0-100):")

# Math marks
while True:
    math = int(input("Math: "))
    if 0 <= math <= 100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100")

# Science marks
while True:
    science = int(input("Science: "))
    if 0 <= science <= 100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100")

# English marks
while True:
    english = int(input("English: "))
    if 0 <= english <= 100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100")

# History marks
while True:
    history = int(input("History: "))
    if 0 <= history <= 100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100")

# Art marks
while True:
    art = int(input("Art: "))
    if 0 <= art <= 100:
        break
    else:
        print("Invalid marks! Please enter marks between 0 and 100")

total_marks = math + science + english + history + art
average = total_marks / 5

if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

print("\n----- STUDENT REPORT CARD -----")
print(f"Student Name: {name}")
print("\nMarks:")
print(f"Math: {math}")
print(f"Science: {science}")
print(f"English: {english}")
print(f"History: {history}")
print(f"Art: {art}")
print(f"\nTotal Marks: {total_marks}")
print(f"Average: {average}")
print(f"Grade: {grade}")
print("----------------------------")