def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

grade1, grade2, grade3 = map(float, input().split())

print(calculate_average(grade1, grade2, grade3))