def interest_calc (balance, annualInterestRate, monthlyPaymentRate):
    """
    interest_calc calculates the remaining balance on a loan after one year
    Arguments:
    balance = outstanding balance on the loan
    annualInterestRate = annual interest rate as a decimal
    monthlyPaymentRate = minimum monthly payment rate as a decimal
    """
    month = 0
    unpaidBalance = 0.0
    unpaidBalance = balance - (balance * monthlyPaymentRate)
    payment = 0.0
    while month < 12:
        unpaidBalance = (unpaidBalance - payment) + (annualInterestRate / 12.0) * (unpaidBalance - payment)
        month += 1
        #print("Month " + str(month) + " Remaining balance: " + str(unpaidBalance))
        payment = (unpaidBalance * monthlyPaymentRate)
    return "Remaining balance: " + str(round(unpaidBalance, 2))

print(interest_calc(484, 0.2, 0.04))
