# 8. Take values of length and breadth of a rectangle from user and check if it is square or not.


length, breadth = input("Enter length and breadth values(separated by space): ").split()

if int(length)==int(breadth):
    print("Its Square")
else:
    print("Its Rectangle ")