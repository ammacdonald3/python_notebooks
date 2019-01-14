initial_balance = 4773
interest = 0.2
balance = initial_balance
month = 0
payment = 10

while True:
    while month < 12:
        balance = balance + (balance * (interest/12)) - (payment)
        month += 1
    if balance <= 0:
        print("Lowest Payment: " + str(payment))
        break
    payment += 10
    balance = initial_balance
    month = 0
