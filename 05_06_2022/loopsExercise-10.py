#  10. A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#  Ask user for their salary and year of service and print the net bonus amount.


salary = int(input("Enter your current salary: "))
experience = int(input("Enter your experience: "))

if experience > 5:
    bonus = salary*0.05
    print()
    print(f"congratulation your bonus is ₹ {round(bonus)}")
    print()
else:
    print("Sorry no bonus")
