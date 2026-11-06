# Employee Payroll and Deduction Analysis

print("===== EMPLOYEE PAYROLL SYSTEM =====")

# Employee Details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

# Salary Details
basic = float(input("Enter Basic Salary: "))
hra = float(input("Enter House Rent Allowance: "))
da = float(input("Enter Dearness Allowance: "))
overtime_hours = float(input("Enter Overtime Hours: "))
overtime_rate = float(input("Enter Overtime Rate per Hour: "))
incentive = float(input("Enter Incentive Amount: "))

# Validate Inputs
if min(basic, hra, da, overtime_hours,
       overtime_rate, incentive) < 0:
    print("Invalid Salary Details!")

else:
    # Calculate Overtime
    overtime = overtime_hours * overtime_rate

    # Calculate Gross Salary
    gross_salary = basic + hra + da + overtime + incentive

    # Calculate Progressive Deductions
    if gross_salary <= 20000:
        deduction = gross_salary * 0.05

    elif gross_salary <= 40000:
        deduction = (20000 * 0.05) + ((gross_salary - 20000) * 0.10)

    elif gross_salary <= 60000:
        deduction = (20000 * 0.05) + (20000 * 0.10) + ((gross_salary - 40000) * 0.15)

    else:
        deduction = (20000 * 0.05) + (20000 * 0.10) + (20000 * 0.15) + ((gross_salary - 60000) * 0.20)

    # Calculate Net Salary
    net_salary = gross_salary - deduction

    # Display Salary Statement
    print("\n========== SALARY STATEMENT ==========")
    print("Employee Name       :", name)
    print("Employee ID         :", emp_id)
    print("--------------------------------------")
    print("Basic Salary        : Rs.", basic)
    print("House Rent Allowance: Rs.", hra)
    print("Dearness Allowance  : Rs.", da)
    print("Overtime Amount     : Rs.", overtime)
    print("Incentives          : Rs.", incentive)
    print("--------------------------------------")
    print("Gross Salary        : Rs.", gross_salary)
    print("Total Deduction     : Rs.", deduction)
    print("--------------------------------------")
    print("Net Salary          : Rs.", net_salary)
    print("======================================")
