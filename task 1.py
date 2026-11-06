# University Scholarship Allocation System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nEnter details of Student", i + 1)

    name = input("Enter student name: ")
    aggregate = float(input("Enter aggregate marks: "))

    subject1 = float(input("Enter Subject 1 marks: "))
    subject2 = float(input("Enter Subject 2 marks: "))
    subject3 = float(input("Enter Subject 3 marks: "))

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter annual family income: "))

    # Eligibility checking
    if (aggregate >= 75 and
        subject1 >= 60 and
        subject2 >= 60 and
        subject3 >= 60 and
        attendance >= 75 and
        income <= 250000):

        students.append({
            "name": name,
            "aggregate": aggregate,
            "attendance": attendance,
            "income": income,
            "core": subject1 + subject2 + subject3
        })

    else:
        print(name, "is Not Eligible")

# Ranking eligible students
students.sort(
    key=lambda x: (
        -x["aggregate"],
        -x["attendance"],
        -x["core"],
        x["income"],
        x["name"].lower()
    )
)

# Scholarship allocation
seats = int(input("\nEnter number of scholarship seats: "))

print("\n--- SCHOLARSHIP RESULTS ---")

for i, student in enumerate(students):
    if i < seats:
        print(i + 1, student["name"], "- Selected")
    else:
        print(i + 1, student["name"], "- Not Selected")

print("\nTotal Eligible Students:", len(students))
print("Total Scholarships:", min(seats, len(students)))
