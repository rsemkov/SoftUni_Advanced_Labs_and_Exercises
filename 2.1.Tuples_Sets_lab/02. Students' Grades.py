students_count = int(input())
students_grades = {}

for _ in range(students_count):
    student, grade = input().split()
    if student not in students_grades.keys():
        students_grades[student] = []
    students_grades[student].append(float(grade))

for student_name, student_grade in students_grades.items():
    average_grade = sum(student_grade) / len(student_grade)
    conv_to_str = " ".join(list(map(lambda x: f"{x:.2f}", student_grade)))
    print(f"{student_name} -> {conv_to_str} (avg: {average_grade:.2f})")
