def calculate_average(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3

grade1 = float(input("Enter the first grade "))
grade2 = float(input("Enter the second grade "))
grade3 = float(input("Enter the third grade "))

print(calculate_average(grade1, grade2, grade3))