#Write a python function to identify and return the number name of a given number. 
#The number should be in the range 1 to 1000. If the number is invalid, return -1.

#lex_auth_0127136373866577921209

def integer_to_english(number):
    #start writing your code here
    l = len(number)
    
    if(l == 0):
        print("empty string")
        return
    
    if (l > 4):
        print("Length more than 4 is not supposed")
        return
    
    single_digits = ["zero", "one", "two", "three", "four", "five","six", "seven", "eight", "nine"]
    two_digits = ["", "ten", "elven", "twelve", "thirteen", "fourteen", "fifteen","sixteen", "seventeen", "eighteen", "nineteen"]
    tens_multiply = ["", "", "twenty","thirty", "fourty", "fifty", "sixty", "sevnty", "eighty", "ninety"]
    tens_power = ["hundred", "thousand"]
number=789
print(integer_to_english(number))
