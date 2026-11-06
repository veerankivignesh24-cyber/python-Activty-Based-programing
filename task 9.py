# Multi-Currency Travel Budget Analysis

print("======= TRAVEL BUDGET ANALYSIS =======")

# Input budget details
budget = float(input("Enter total travel budget (INR): "))
n = int(input("Enter number of expense categories: "))

total_expenses = 0
expenses = {}

for i in range(n):
    print("\nExpense Category", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount: "))
    currency = input("Enter currency (USD/EUR/INR): ").upper()

    # Exchange rates (example rates)
    if currency == "USD":
        rate = 88.50
    elif currency == "EUR":
        rate = 102.00
    elif currency == "INR":
        rate = 1.00
    else:
        print("Invalid currency! Try again.")
        continue

    # Conversion fee
    fee_rate = 2
    converted_amount = amount * rate
    conversion_fee = converted_amount * fee_rate / 100

    # Total expense in INR
    final_amount = converted_amount + conversion_fee

    expenses[category] = final_amount
    total_expenses += final_amount

    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(conversion_fee, 2))
    print("Total Expense: Rs.", round(final_amount, 2))

# Find largest expense category
if expenses:
    largest_category = max(expenses, key=expenses.get)
    largest_expense = expenses[largest_category]
else:
    largest_category = "None"
    largest_expense = 0

# Calculate remaining budget
remaining_budget = budget - total_expenses

# Final report
print("\n======= FINAL TRAVEL REPORT =======")
print("Travel Budget       : Rs.", round(budget, 2))
print("Total Expenses      : Rs.", round(total_expenses, 2))
print("Remaining Budget    : Rs.", round(remaining_budget, 2))

print("\nLargest Expense Category:", largest_category)
print("Largest Expense Amount: Rs.", round(largest_expense, 2))

if total_expenses <= budget:
    print("\nStatus: Travel expenses are within budget.")
else:
    print("\nStatus: Travel expenses exceed the budget.")

print("===================================")
print("       HAPPY JOURNEY!")
