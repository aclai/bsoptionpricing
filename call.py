import numpy as np
from scipy.stats import norm

def call(S,K,r,t,sd):
    
    #d1
    di = (1/(sd*(t**(1/2))))*(np.log(S/K)+((r+((sd**2)/2))*t))
    #d2
    dii = di-(sd*(t**(1/2)))
    #N(d1)
    Ndi = norm.cdf(di)
    #N(d2)
    Ndii = norm.cdf(dii)
    #discount factor e^(-rt)
    D = np.exp(-r*t)
    #print(di, dii, Ndi, Ndii, D)

    price = (S*Ndi)-(K*D*Ndii)

    return price
