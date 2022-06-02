# 2. Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

string = input("Enter a String: ")
output1 = {i: string.count(i) for i in string}
output2 = {}
for key, value in output1.items():
    if key not in output2.keys():
        output2[key] = value

output3 = sorted(output2.items(), key=lambda x: x[1], reverse=True)
print(dict(output3))