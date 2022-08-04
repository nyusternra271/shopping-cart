# shopping_cart.py
import os
from dotenv import load_dotenv

load_dotenv()


from pandas import read_csv

products_df = read_csv('products.csv')
products = products_df.to_dict('records')
store = {
        "name": "Super Cheap Number 1 Grocery Store",
        "phone": "123-456-7890",
        "website": "https://www.stern.nyu.edu"
}

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output
item_ids = [str(product['id']) for product in products]


#print(products)

selections = []
item=''

print('Enter shopping cart items, 1 at a time, entering DONE when finished')
while item.lower() != 'done':
    item=input('Please input a product: ')
    if (item.lower() != 'done') and (item not in item_ids):
        print("Hey, are you sure that product identifier is correct? Please try again:")
    elif item.lower() != 'done':
     selections.append(item)
print("-------------------------")
print(store['name']+ "\n"+store['phone']+ "\n" + store['website'])
print("-------------------------")

# The following code was adapted from these webpages:
# 1. https://www.programiz.com/python-programming/datetime/current-datetime
# 2.  https://stackoverflow.com/questions/1759455/how-can-i-account-for-period-am-pm-using-strftime

from datetime import datetime
now = datetime.now()

dt_string=now.strftime("%Y/%m/%d %I:%M %p")
print("CHECKOUT AT:", dt_string)


subtotal = 0.00
email_receipt_dict = { "total_price_usd": "",
                       "store_name": store['name'],
                       "store_website": store['website'],
                       "store_phone_number": store['phone']
}

selection_dict = {}
my_list = []
for selection in selections:
    for product in products:
        if str(product['id']) == selection:
            print(product['name'], to_usd(product['price']))
            subtotal += product['price']
            selection_dict['id'] = int(selection)
            # referenced this page with respect to appending to a list of dictionaries:
            #  https://www.askpython.com/python/list/list-of-dictionaries
            selection_dict['name'] = product['name']
            # got the idea to use the copy method from this page: https://www.geeksforgeeks.org/appending-a-dictionary-to-a-list-in-python/
            my_list.append(selection_dict.copy()) 
print("-------------------------")

tax_rate = float(os.getenv("TAX_RATE"))
print('SUBTOTAL:', to_usd(subtotal))
print('TAX:', to_usd(tax_rate*subtotal))
total = subtotal * (1+tax_rate)
print('TOTAL:', to_usd(total))

print("-------------------------")

template_data = {
    "total_price_usd": to_usd(total),
    "store_name": store['name'],
    "store_website": store['website'],
    "store_phone_number": store['phone'],
    "human_friendly_timestamp": dt_string,
    "products": my_list
}

email_option = input("Would you like a copy of your receipt sent to you via email?")

if email_option.lower() == "yes":
    recipient_address = input("Please enter your email address:")
    print("-------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
else:
    print("THANKS, SEE YOU AGAIN SOON")
print("-------------------------")