# 19. From a list containing ints, strings and floats, make three lists to store them separately

mixed_list = ['hello', 'world', 'musaddiq', 'python', 10, 12, 14, 16, 18, 12.2, 14.4, 16.6, 18.8]

string_type = [i for i in mixed_list if type(i) == str]
print(string_type)
int_type = [i for i in mixed_list if type(i) == int]
print(int_type)
float_type = [i for i in mixed_list if type(i) == float]
print(float_type)
