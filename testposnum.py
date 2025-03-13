def testposnum(x):
    
    while True:
        try:
            x = float(x)
            if x < 0:
                raise ValueError
            break
        
        except ValueError:
            x = input("Please input a positive number:")
        
    return x
