# -*- coding: utf-8 -*-

import mod
print("Welcome to", mod.shop_name)
print("Available sizes:", mod.coffee_sizes)
print("Available roasts:", mod.coffee_roasts)

# Get some inputs from the user
order_size = input("What size coffee do you want? ")
order_roast = input("What roast do you want? ")

# Send the order to the coffee shop module
shop_says = mod.order_coffee(order_size, order_roast)
# Print out whatever it gave back to us
print(shop_says)