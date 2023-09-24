def calculate_grade(marks):

  grade = ""

  if marks < 25:
    grade = "F"
  elif marks >= 25 and marks < 45:
    grade = "E"
  elif marks >= 45 and marks < 50:
    grade = "D"
  elif marks >= 50 and marks < 60:
    grade = "C"
  elif marks >= 60 and marks < 80:
    grade = "B"
  elif marks >= 80:
    grade = "A"

  return grade

marks = int(input("Enter the student's marks: "))

grade = calculate_grade(marks)

print(f"The student's grade is {grade}.")
