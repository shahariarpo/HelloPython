has_good_credit = True

price = 1000000
if has_good_credit:
    down_payment = price * 0.1
else:
    down_payment = price * 0.2
print(f"Your down payment is: ${down_payment}")
