import argparse
from decimal import Decimal

parser = argparse.ArgumentParser()
parser.add_argument("spot", help="spot price of the underlying asset", type=float)
parser.add_argument("strike", help="strike price of the option", type=float)
parser.add_argument("option", choices=["call", "put"], help="choose call or put option")
args = parser.parse_args()

spot = args.spot
strike = args.strike
        
if args.option == "call":
    if args.spot <= args.strike:
        print("The call option is out of the money, and it is worth $0.")
    else:
        price = Decimal(str(spot)) - Decimal(str(strike))
        print(f"The price of the call option should be $ {price}.")

elif args.option == "put":
    if args.spot >= args.strike:
        print("The put option is out of the money, and it is worth $0.")
    else:
        price = Decimal(str(strike)) - Decimal(str(spot))
        print(f"The price of the put option should be $ {price}.")
