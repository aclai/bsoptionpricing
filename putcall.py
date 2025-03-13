def putcall():    
    
    x = input("Is it a call or put option[c/p]?")
    
    if x != "c" and x != "p":
        print ("Please choose call[c] or put[p]:")
        x = putcall()        

    return x
 
