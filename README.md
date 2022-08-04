# Shopping Cart Project

## Introduction

This application prompts you to select from a group of products and displays the list of goods selected along with a subtotal, tax (if applicable), and total. The user also has the option of having a copy of the receipt sent via email.

## Requirements:

1. Create a new environment for running this program as follows:

```sh
conda create -n shopping-cart python=3.10
```
2. Install the pandas, dotenv and sendgrid packages by running the following command:

```sh
pip install -r requirements.txt
```

3. Set up your own .env file that contains the tax rate for your locale along with your SendGrid sender address, API key and template ID (more on these in the next step):

```sh
TAX_RATE = "Your local sales tax rate (e.g., 0.0875) here"
SENDER_ADDRESS="Your sender email address here"
SENDGRID_API_KEY="Your API key here"
SENDGRID_TEMPLATE_ID="Your SendGrid template ID here"
```
modify the value of the TAX_RATE variable as needed

4. Sign up for a Sendgrid account so that you can create a template and API key that will be used for sending the receipt via email:
    1. Go to https://signup.sendgrid.com and register using an email address of your choosing (using a Gmail account is recommended due to possible issues with school or employer email domains)
    2. Follow the instructions to complete the "Single Sender Verification" by clicking the link in the confirmation email you received (remember to check your spam folder if you don't see this email in a timely fashion). You can also access this utility via the Settings menu (Settings->Sender Authentication) from your dashboard after logging in.
    3. Set up a template by navigating to https://sendgrid.com/dynamic_templates or through the Email API menu (Email API->Dynamic Templates) from your dashboard:
        a. Click the "Create Template" button and give your template a descriptive name
        b. Click "Save". You should your template's unique identifier - copy it and add it to the .env file you created in the step above - it should be assigned to the SENDGRID_TEMPLATE_ID variable
        c. Click "Add Version" to continue
        d. Select "Code Editor" to continue
        e. Add the following between the <div></div> block:
        ```sh
         <img src="https://www.shareicon.net/data/128x128/2016/05/04/759867_food_512x512.png">

        <h3>Your Receipt from the No 1 Super Value Grocery Store</h3>

        <p>Date: {{human_friendly_timestamp}}</p>
        <ul>
        {{#each products}}
    	<li>You ordered: ... {{this.name}}</li>
        {{/each}}
        </ul>

        <p>Total: {{total_price_usd}}</p>
            <p style="font-size:12px; line-height:20px;">
                <a class="Unsubscribe--unsubscribeLink" href="{{{unsubscribe}}}" target="_blank" style="font-family:sans-serif;text-decoration:none;">
                    Unsubscribe
                </a>
          -
          <a href="{{{unsubscribe_preferences}}}" target="_blank" class="Unsubscribe--unsubscribePreferences" style="font-family:sans-serif;text-decoration:none;">
            Unsubscribe Preferences
          </a>
        </p>
        ```

    4. Finally, configure the template's subject by clicking on "Settings" in the left sidebar. Choose an email subject like "Your Receipt from the Super Duper Grocery Store". Then click "Save Template".


5. Create your products.csv file inside the data directory. The file structure should resemble the following:
```sh
id,name,aisle,department,price
1,Chocolate Sandwich Cookies,cookies cakes,snacks,3.5
2,All-Seasons Salt,spices seasonings,pantry,4.99
3,Robust Golden Unsweetened Oolong Tea,tea,beverages,2.49
4,Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce,frozen meals,frozen,6.99
5,Green Chile Anytime Sauce,marinades meat preparation,pantry,7.99
6,Dry Nose Oil,cold flu allergy,personal care,21.99
7,Pure Coconut Water With Orange,juice nectars,beverages,3.5
8,Cut Russet Potatoes Steam N\' Mash,frozen produce,frozen,4.25
9,Light Strawberry Blueberry Yogurt,yogurt,dairy eggs,6.5
10,Sparkling Orange Juice & Prickly Pear Beverage,water seltzer sparkling water,beverages,2.99
11,Peach Mango Juice,refrigerated,beverages,1.99
12,Chocolate Fudge Layer Cake,frozen dessert,frozen,18.5
13,Saline Nasal Mist,cold flu allergy,personal care,16
14,Fresh Scent Dishwasher Cleaner,dish detergents,household,4.99
15,Overnight Diapers Size 6,diapers wipes,babies,25.5
16,Mint Chocolate Flavored Syrup,ice cream toppings,snacks,4.5
17,Rendered Duck Fat,poultry counter,meat seafood,9.99
18,Pizza for One Suprema  Frozen Pizza,frozen pizza,frozen,12.5
19,Gluten Free Quinoa Three Cheese & Mushroom Blend,grains rice dried goods,dry goods pasta,3.99
20,Pomegranate Cranberry & Aloe Vera Enrich Drink,juice nectars,beverages,4.25
```


## Running This App

After downloading this repo, you can run it as follows:

1. Browse to the directory where you saved all of the files.
2. Activate the conda environment you created earlier:
```sh
conda activate shopping-cart
```
3. Run the program:
```sh
python -m app.shopping_cart
```

If all is set up properly, you should see the following:

![Initial Sxcreenshot When Running the App](https://github.com/nyusternra271/miscellaneous/blob/main/screen-1.png)

You should see something like the following after entering a few selections:

![Second Screenshot When Running the App](https://github.com/nyusternra271/miscellaneous/blob/main/screenshot-2.png)