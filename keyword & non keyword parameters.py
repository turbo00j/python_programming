"""
keyword and non keyword parameters
"""


def person_details(firstname,lastname,emailID,mobile):
    print("First name:",firstname,"\nlast name:",lastname,"\nemail ID",emailID,"\nmobile:",mobile)
person_details('raju',emailID='jaideep@gmail.com',lastname='kumar',mobile=7885896445)
# raju = non keyword parameter
# remaining three are keyword parameters because they contain parameter name as a keyword
