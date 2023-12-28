#1. Function Defination is one time process
def addFourNumber(a,b,c,d): #a,b,c,d are formalargument
    # Every Number May Result Something
    return a + b + c + d

#2. Function Calling/Invoking is many time process
result=addFourNumber(10.4,1.3,2.7,5.9) # I am sending float value(decimal) as actualargument
print(result)