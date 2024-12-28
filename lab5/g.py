import re
test_str = 'geeksforgeeks_is_best'
print("The original string is : " + str(test_str))
temp = re.split('_+', test_str)
# using lambda function to convert first letter of every word to uppercase except for first word
res = temp[0] + ''.join(map(lambda x: x.title(), temp[1:]))
print("The camel case string is : " + str(res))
