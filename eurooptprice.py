import argparse
from decimal import Decimal

def call(spot, strike):
    if spot <= strike:
        print("The call option is out of the money, and it is worth $0.")
    else:
        price = Decimal(str(spot)) - Decimal(str(strike))
        print(f"The price of the call option should be $ {price}.")

def put(spot, strike):
    if spot >= strike:
        print("The put option is out of the money, and it is worth $0.")
    else:
        price = Decimal(str(strike)) - Decimal(str(spot))
        print(f"The price of the put option should be $ {price}.")

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("spot", help="spot price of the underlying asset", type=float)
    parser.add_argument("strike", help="strike price of the option", type=float)
    parser.add_argument("option", choices=["call", "put"], help="choose call or put option")
    args = parser.parse_args()

    spot = args.spot
    strike = args.strike
            
    if args.option == "call":
        call(spot, strike)

    elif args.option == "put":
        put(spot, strike)
