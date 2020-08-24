principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
current_month = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    principal = principal * (1 + rate / 12) - payment
    if (current_month >= extra_payment_start_month and current_month <= extra_payment_end_month):
        principal -= extra_payment
        total_paid += extra_payment
    
    total_paid += payment
    current_month += 1
    print(current_month, round(total_paid,2), round(principal, 2))
    
print('Total paid', round(total_paid, 2))
print('Months', current_month - 1)