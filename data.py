from transform import convert_to_ksh

btc_price_usd = [58000, 62000, 70000, 75000]
#print(type(btc_price_usd)) 



btc_prices_ksh = convert_to_ksh(btc_price_usd)
print(btc_prices_ksh)



# exchange_rates = 129
# btc_price_ksh = [price * exchange_rates for price in btc_price_usd ]

# print(btc_price_usd)

# print(btc_price_ksh)





