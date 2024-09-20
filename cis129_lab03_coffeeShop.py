# Author: Devin Easby
# Coffee shop reciept 
# Calculates the cost of Coffee and Muffins including tax
# Prices - This section indicates the price of each item on the menu 
coffee_prices = 5.00 
muffin_prices = 4.00
tax_rate = 0.06
print ('Devins Coffee and Muffin Shop')
#user input - This section will indicate the amount of each item that is being purchased by the consumer.
num_coffees = int(input('Enter the number of Coffees bought'))
num_muffins = int(input('Enter the number of Muffins bought'))
#Calculations - This section will show how calculations are made depending on the item and quantity
subtotal = (num_coffees * coffee_prices) + (num_muffins * muffin_prices)
tax = (subtotal * tax_rate) 
total = (subtotal * tax)
#Receipt - This will provide the consumer of a break down of their purchase 
print ('Devins Coffee and Muffin Shop')
print (f'{num_coffees} Coffee at {coffee_prices} each: ${num_coffees * coffee_prices}')
print (f'{num_muffins} Muffin at {muffin_prices} each: ${num_muffins * muffin_prices}')
print (f'6% tax: {subtotal * tax_rate}')
print ('-----------------------------')
print (f'total: ${total}')
