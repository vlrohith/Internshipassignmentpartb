def calculate_total_cost(quantity, unit_price):
  

  total_cost = quantity * unit_price

  if total_cost > 1000:
    discount = total_cost * 0.1
    total_cost -= discount

  return total_cost


quantity = int(input("Enter the quantity of items purchased: "))


unit_price = 100

total_cost = calculate_total_cost(quantity, unit_price)

print(f"The total cost of the purchase is {total_cost}.")
