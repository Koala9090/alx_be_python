mincome = int(input("Enter your monthly income:"))
mexpenses = int(input("Enter your total monthly expenses"))
msavings = mincome - mexpenses
psavings = msavings * 12 + (msavings*12*0.05)
print("Projected savings after one year, with interest, is:", psavings)
