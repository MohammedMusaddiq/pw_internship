#   12. A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#   Take following input from user
#   Number of classes held
#   Number of classes attended.
#   And print
#   percentage of class attended
#   Is student is allowed to sit in exam or not.


classes_held = int(input("No of classes held: "))
classes_attend = int(input("No of classes attend: "))

percentage = (classes_attend/classes_held)*100

if percentage < 75:
    print(f"Student have attended {round(percentage)}% of class, student cannot allow to sit in exam. ")
else:
    print(f"Student have attended {round(percentage)}% of class, he can sit in exam")
    