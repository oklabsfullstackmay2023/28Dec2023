#1. Function Defination is one time process
def multiplyFiveNumber(a,b,c,d,e): #a,b,c,d,e are formalargument
    # Every Function May Return Something
    return a * b * c * d * e

#2. Function Calling/Invoking is many time process
result=multiplyFiveNumber(5,4,3,2,4)#I am sending integer(wholenumber) value as actualargument
print(result)