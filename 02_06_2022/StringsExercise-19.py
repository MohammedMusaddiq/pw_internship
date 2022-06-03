# 19. Write a Python program to find smallest and largest word in a given string.


string = input("Enter a string: ")

string_list = string.split()
largest_word = string_list[0]
smallest_word = string_list[0]
list_len = len(string_list)

for i in range(list_len):
    if len(largest_word) < len(string_list[i]):
        largest_word = string_list[i]
        list_len += 1
    if len(smallest_word) > len(string_list[i]):
        smallest_word = string_list[i]
        list_len += 1

print(f"The largest word in given string is:  {largest_word}")
print(f"The smallest word in given string is:  {smallest_word}")
