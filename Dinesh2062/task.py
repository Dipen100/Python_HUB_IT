a = input("Enter a string. ")
# while a.isaplha() == True:
# x = a.isalpha()
if a.isalpha() == True:
 print("You have entered a valid string")
else:     
  print("Your input is incorrect")
 

# # for x in a:

# #  print(x)
# for x in (a.count(a)): 
#  print(x)
from collections import Counter
test_str = a
output = Counter(test_str)
# print("the character length is",'\n', output) 
# for y in output:
#   print(y)


print(output)  
#   ,y,':', 
# the character length is" ,