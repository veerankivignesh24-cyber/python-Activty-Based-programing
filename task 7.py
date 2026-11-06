# Retail Billing with Multiple Discount Rules

print("========== RETAIL BILLING SYSTEM ==========")

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

print("\nEnter Product Details")

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/electronics/clothing): ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    amount = price * quantity

    # Category-specific tax
    if category.lower() == "food":
        tax_rate = 5
    elif category.lower() == "electronics":
        tax_rate = 18
    elif category.lower() == "clothing":
        tax_rate = 12
    else:
        tax_rate = 10

    tax = amount * tax_rate / 100
    subtotal += amount
    total_tax += tax

    print("\nProduct:", name)
    print("Quantity:", quantity)
    print("Amount: Rs.", round(amount, 2))
    print("Tax:", tax_rate, "%")
    print("Tax Amount: Rs.", round(tax, 2))

# Discount rules
if subtotal >= 10000:
    discount_rate = 20
elif subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
max_discount = 2000

if discount > max_discount:
    discount = max_discount

# Final bill calculation
final_amount = subtotal + total_tax - discount

# Invoice
print("\n========== FINAL INVOICE ==========")
print("Subtotal          : Rs.", round(subtotal, 2))
print("Total Tax         : Rs.", round(total_tax, 2))
print("Discount Rate     :", discount_rate, "%")
print("Discount Amount   : Rs.", round(discount, 2))
print("-----------------------------------")
print("Final Amount      : Rs.", round(final_amount, 2))
print("===================================")
print("       THANK YOU! VISIT AGAIN")
