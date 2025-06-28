name = input("Enter student name: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
total = sum(marks)
percentage = total / 5
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
else:
    grade = "F"
print("\n----- Student Summary -----")
print("Name:", name)
print("Marks:", marks)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)