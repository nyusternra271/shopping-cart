# shopping_cart.py
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()
# Reference for the Sendgrid code: 
# https://github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md#email-templates
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
client = SendGridAPIClient(SENDGRID_API_KEY)
from pandas import read_csv

# This usage of the os.path.join method was taken from Prof. Rossetti's documentation here:
# https://github.com/prof-rossetti/intro-to-python/blob/main/projects/shopping-cart/challenges.md

csv_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
products_df = read_csv(csv_filepath)
products = products_df.to_dict('records')
store = {
        "name": "No 1 Super Value Grocery Store",
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
# 3. https://www.programiz.com/python-programming/datetime/strftime

from datetime import datetime
now = datetime.now()

dt_string=now.strftime("%A %D %I:%M %p")
print("CHECKOUT AT:", dt_string)


subtotal = 0.00

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

email_option = input("Would you like a copy of your receipt sent to you via email? ")

if email_option.lower() == "yes":
    recipient_address = input("Please enter your email address: ")
    message = Mail(from_email=SENDER_ADDRESS, to_emails=recipient_address)
    message.template_id = SENDGRID_TEMPLATE_ID
    message.dynamic_template_data = template_data
    try:
        response = client.send(message)
        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as err:
        print(type(err))
        print(err)
    print("-------------------------")
    print("THANKS, SEE YOU AGAIN SOON!")
else:
    print("-------------------------")
    print("THANKS, SEE YOU AGAIN SOON")

print("-------------------------")