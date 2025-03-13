#calculated the price of a European Call or Put option based on the Black-Scholes pricing model

from putcall import putcall
from call import call
from put import put
from testposnum import testposnum

#def optprice():
    
#determine whether the option in question is a put or call
putcall = putcall()

#asking for current market price
S = input("What is the spot price of the underlying asset?")
#test if user input is a number that is bigger or equal to 0
S = testposnum(S)
print("spot price =", S)

#ask for strike price
K = input("What is the strike price?")
#test if user input is a number that is bigger or equal to 0
K = testposnum(K)
print("spot price =", S, "strike price =", K)

#ask for risk-free rate
r = input("What is the risk-free rate[in decimal]?")
#test if user input is a number that is bigger or equal to 0
r = testposnum(r)
print("spot price =", S, "strike price =", K, "risk-free rate =", r)

#ask for time to expiration in years
t = input("What is the time to expiration in year(s)[x/365]?")
#test if user input is a number that is bigger or equal to 0
t = testposnum(t)
print("spot price =", S, "strike price =", K, "risk-free rate =", r, "time to expriation =",t)

#ask for standard deviation
sd = input("What is the standard deviation of the continuously compunded annual returns of the underlying asset?")
#test if user input is a number that is bigger or equal to 0
sd = testposnum(sd)
print("spot price =", S, "strike price =", K, "risk-free rate =", r, "time to expriation =",t, "standard deviation =", sd)


#calculate
if putcall == "c":
    price = call(S,K,r,t,sd)
else:
    price = put(S,K,r,t,sd)

#print answer
print ("The price of the option is $", price)

