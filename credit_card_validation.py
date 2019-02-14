# Enter your code here. Read input from STDIN. Print output to STDOUT
#Importing the regular expression library
import re

# N refers to the first line of input contains an integer . 
#sequence refers to the credit card numbers which N will contain.

# This a manual initializaion of total no. of credit cards & their values w.r.t hackerrank execution format

N=6
sequence=["4123456789123456","5123-4567-8912-3456","61234-567-8912-3456","4123356789123456","5133-3367-8912-3456","5123 - 3567 - 8912 - 3456"]

def credit_card_validation(value):

    o1 = re.match(r"^[456]\d{15}$", value)
    o2 = re.match(r"^[456]\d{3}-\d{4}-\d{4}-\d{4}$",value)
    value = value.replace("-","")
    o3 = re.match(r"(?!.*(\d)(-?\1){3})",value)
    if (o1 or o2) and o3:
        print("Valid")
    else:
        print("Invalid")

# Comment below lines for Interactice User Inputs		

if N>0 and N<100:
    for i in range(0,N):
        value=str(sequence[i])
        credit_card_validation(value)
       
# Uncommment below lines for Interactice User Inputs

# N=int(input("enter the number of inputs"))
# if N>0 and N<100:
#     for i in range(N):
#         value=input("enter the credit number you need to validate")
#         credit_card_validation(value)

