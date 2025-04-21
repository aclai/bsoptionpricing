"""
This will calculate the value of a position on an European option on the expiration day.

Usage:
python eurooptprice.py [-h] -sp SPOT -st STRIKE -o {call,put} -p {long,short} 

Example 1:
If one holds a long position on a call option with a strike price of $10 and spot price of $20 - python eurooptprice.py -sp 20 -st 10 -o call -p long

Example 2:
If one holds a short position on a put option with a strike price of $30 and spot price of $25 - python eurooptprice.py -sp 25 -st 30 -o put -p short
"""
import argparse
from decimal import Decimal
def call(spot, strike, position):
    if spot <= strike:
        print("The call option is out of the money, and your position is $0.")
    else:
        price = Decimal(str(spot)) - Decimal(str(strike))
        if position == "long":
            print(f"A long position of the call option should be $ {price}.")
        else:
            print(f"A short position of the call option should be $ {-price}.")
def put(spot, strike, position):
    if spot >= strike:
        print("The put option is out of the money, and your position is $0.")
    else:
        price = Decimal(str(strike)) - Decimal(str(spot))
        if position == "long":
            print(f"A long position of the put option should be $ {price}.")
        else:
            print(f"A short position of the put option should be $ {-price}.")
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-sp", "--spot", help="spot price of the underlying asset", type=float, required=True)
    parser.add_argument("-st", "--strike", help="strike price of the option", type=float, required=True)
    parser.add_argument("-o", "--option", choices=["call", "put"], help="choose call or put option", required=True)
    parser.add_argument("-p", "--position", choices=["long", "short"], help="choose long or short position", required=True)
    args = parser.parse_args()
    spot = args.spot
    strike = args.strike
    position = args.position
    if args.option == "call":
        call(spot, strike, position)
    elif args.option == "put":
        put(spot, strike, position)
