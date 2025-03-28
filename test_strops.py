import Strops
 
print("-"*80)

print("Program for getAllSpans")
input_string = input("Enter the string: ")
substring = input("Enter the substring: ")
count, span = Strops.getAllSpans(input_string, substring)
print(count, span)

print("Program for reverseWords")
input_string = input("Enter the string: ")
Strops.reverseWords(input_string)

print("Program for removePunctuation")
input_string = input("Enter the string: ")
Strops.removePunctuation(input_string)

print("Program for countWords")
input_string =  input("Enter the string: ")
Strops.countWords(input_string)

print("Program for charecterMap")
input_string =  input("Enter the string: ")
Strops.charecterMap(input_string)

print("Program for makeTitle")
input_string =  input("Enter the string: ")
Strops.makeTitle(input_string)

print("Program for normalizeSpaces")
input_string =  input("Enter the string: ")
Strops.normalizeSpaces(input_string)

print("Program for transform")
input_string =  input("Enter the string: ")
Strops.transform(input_string)

print("Program for get_permutations")
input_string =  input("Enter the string: ")
Strops.get_permutations(input_string)