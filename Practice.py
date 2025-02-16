grades = [
    [3, 4, 4, 5, 3],
    [4, 4, 3, 5],
    [5, 4, 3],
    [5, 5, 3, 5, 5],
    [2, 4, 5, 3]
]

students = {
    'Andrey',
    'Danil',
    'Darya',
    'Arina',
    'Max',
}

students_list = list(students)
students_list.sort()

avg_grades = (
    sum(grades[0]) / len(grades[0]),
    sum(grades[1]) / len(grades[1]),
    sum(grades[2]) / len(grades[2]),
    sum(grades[3]) / len(grades[3]),
    sum(grades[4]) / len(grades[4])
)

students_avg_grade = dict(zip(students_list, avg_grades))
print(students_avg_grade)
