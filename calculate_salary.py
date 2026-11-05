# Get the info from the employee
name = input("Enter employee name: ")
# Get the number of hours worked from the employee
hours_worked = float(input("Enter number of hours worked: "))
# Get the hourly pay rate from the employee
pay_rate = float(input("Enter hourly pay rate: "))
print("---------------------------------")
print(f"Employee Name: {name}")
print()
# Evaluate the overtime pay and regular pay
if hours_worked > 40:
# Calculate the overtime the employee worked
overtime_hours = hours_worked - 40
# Calculate the overtime pay of the employee
overtime_pay = overtime_hours * (pay_rate * 1.5)
# Calculate the regular pay of the employee
regular_pay = 40 * pay_rate
# Calculate the gross pay of the employee
gross_pay = regular_pay + overtime_pay
# Calculate the regular pay and gross pay if the employee did not work overtime
else:
overtime_pay = 0
overtime_hours = 0
gross_pay = hours_worked * pay_rate
print()
# Display all of the information to the employee
print("---------------------------------")
print(f"Employee Name: {name}")
print()
print(f'{"Hours Worked":<15}{"Pay Rate":<12}{"OverTime":<12}{"OverTime Pay":<15}
{"RegHour Pay":<15}{"Gross Pay":<12})')
print("----------------------------------------------------------------------------
-----------------------------------")
print(f"{hours_worked:<15}{pay_rate:<12}{overtime_hours:<12.2f}{overtime_pay:<15}$
{regular_pay:<15}${gross_pay:<12}")
