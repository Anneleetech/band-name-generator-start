print("Welcome to tip calculator!")
bill=float(input("how much was the bill?$"))
tip=int(input("What% would want to pay as a tip? 10,12,15?"))
people=int(input("how many of you?"))
bill_of_tip=float(bill/people)*(1+(tip/100))
print(round(float(bill_of_tip),2))
print("{:.2f}".format(bill_of_tip))