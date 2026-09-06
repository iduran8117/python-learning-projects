# Use this code to calculate how much it would cost to order from an online website
# The pricing like discounts and shipping depend on whether or not you are a member.

price=float(input("What is the price of the item?: "))
quantity=int(input("How many items are you purchasing?: "))
is_member=input("Are you a member? (Y/N): ")

sub_total= price * quantity

if is_member== "Y" : 
    discount_amount= sub_total* 0.1

else: 
    discount_amount= 0
after_discount = sub_total - discount_amount

if sub_total>= 100 :
   shipping= 0
else:
    shipping= 8.99

tax_rate= 0.0825
tax= after_discount * tax_rate

final_total= after_discount + tax + shipping

if final_total>=200:
    order_type="Large order"
else:
    order_type="Standard order"

print(f"Subtotal: ${sub_total:.2f}.")
print(f"Discount amount: ${discount_amount:.2f}.")
print(f"Price after discount: ${after_discount:.2f}.")
print(f"Shipping cost: ${shipping:.2f}.")
print(f"Tax: ${tax:.2f}")
print(f"Final total: ${round(final_total,2)}")
print(f"Order type: {order_type}")