# Manufacturing Cost and Profitability Analysis

print("======= MANUFACTURING COST ANALYSIS =======")

# Input details
product = input("Enter product name: ")
quantity = int(input("Enter production quantity: "))

material_cost = float(input("Enter material cost per unit: "))
labour_cost = float(input("Enter labour cost per unit: "))
machine_cost = float(input("Enter machine cost per unit: "))

wastage_rate = float(input("Enter wastage percentage: "))
selling_price = float(input("Enter selling price per unit: "))

profit_target = float(input("Enter expected profit percentage: "))

# Calculate material cost
total_material = material_cost * quantity

# Calculate wastage cost
wastage_cost = total_material * wastage_rate / 100

# Calculate labour cost
total_labour = labour_cost * quantity

# Calculate machine cost
total_machine = machine_cost * quantity

# Calculate total manufacturing cost
total_cost = total_material + wastage_cost + total_labour + total_machine

# Calculate selling revenue
total_revenue = selling_price * quantity

# Calculate profit
profit = total_revenue - total_cost

# Calculate profit percentage
profit_percentage = (profit / total_cost) * 100 if total_cost > 0 else 0

# Display report
print("\n======= MANUFACTURING REPORT =======")
print("Product Name          :", product)
print("Production Quantity   :", quantity)
print("Material Cost         : Rs.", round(total_material, 2))
print("Wastage Cost          : Rs.", round(wastage_cost, 2))
print("Labour Cost           : Rs.", round(total_labour, 2))
print("Machine Cost          : Rs.", round(total_machine, 2))
print("------------------------------------")
print("Total Manufacturing Cost: Rs.", round(total_cost, 2))
print("Total Selling Revenue   : Rs.", round(total_revenue, 2))
print("Total Profit            : Rs.", round(profit, 2))
print("Profit Percentage       :", round(profit_percentage, 2), "%")

# Check profit target
print("\n======= PROFIT ANALYSIS =======")

if profit_percentage >= profit_target:
    print("Production meets the profit target.")
else:
    print("Production does not meet the profit target.")

print("Expected Profit Target:", profit_target, "%")
print("====================================")
