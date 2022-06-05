#  9. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#  Ask user for quantity
#  Suppose, one unit will cost 100.
#  Judge and print total cost for user.

quantity = input(("Enter the quantity: "))
cost = 100*int(quantity)
if cost > 1000:
    discounted_price = cost-(cost*0.1)
    print(f"Your total price is ₹ {round(cost)}")
    print(f"10% discount - ₹ {round(cost*0.1)}")
    print(f"Final price With discount - ₹ {round(discounted_price)}")

else:
    print(f"Your total price is ₹ {round(cost)}")
