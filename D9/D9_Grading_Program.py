student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for student in student_scores:
    if 100 >= student_scores[student] >= 91:
        grade = "Outstanding"
        student_grades[student] = grade
    if 90 >= student_scores[student] >= 81:
        grade = "Exceeds Expectations"
        student_grades[student] = grade
    if 80 >= student_scores[student] >= 71:
        grade = "Acceptable"
        student_grades[student] = grade
    if student_scores[student] <= 70:
        grade = "Fail"
        student_grades[student] = grade
print(student_grades)