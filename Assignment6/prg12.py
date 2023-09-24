def calculate_attendance_percentage(classes_held, classes_attended):

  attendance_percentage = classes_attended / classes_held * 100
  return attendance_percentage


def check_if_student_is_allowed_to_sit_in_exam(attendance_percentage):
 
  return attendance_percentage >= 75


classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = calculate_attendance_percentage(classes_held, classes_attended)

if check_if_student_is_allowed_to_sit_in_exam(attendance_percentage):
  print("The student is allowed to sit in the exam.")
else:
  print("The student is not allowed to sit in the exam.")
