initial_balance = 320000
annual_interest = 0.2
monthly_interest = annual_interest / 12
balance = initial_balance
month = 0
payment = 0
payment_low = 0
payment_high= 0

while True:
    payment_low = (balance / 12)
    payment_high = (balance * (1 + monthly_interest)**12 / 12.0)
    payment = (payment_low + payment_high) / 2
    while month < 12:
        balance = balance + (balance * monthly_interest) - (payment)
        month += 1
    if balance <= 0:
        print("Lowest Payment: " + str(payment))
        break
    print(payment)
    #payment += 0.01
    balance = initial_balance
    month = 0
    
    
