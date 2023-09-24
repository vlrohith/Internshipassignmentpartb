def calculate_bonus(salary, years_of_service):

  bonus = 0

  if years_of_service > 5:
    bonus = salary * 0.05

  return bonus

salary = int(input("Enter the employee's salary: "))
years_of_service = int(input("Enter the employee's years of service: "))

bonus = calculate_bonus(salary, years_of_service)

print(f"The employee's bonus amount is {bonus}.")
