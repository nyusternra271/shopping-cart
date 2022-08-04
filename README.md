# shopping-caart
Shopping Cart Project

## Introduction

This application prompts you to select from a group of products and displays the list of goods selected along with a subtotal, tax (if applicable), and total. The user also has the option of having a copy of the receipt sent via email.

## Requirements:

1. Create a new environment for running this program as follows:

```sh
conda create -n shopping-cart python=3.10
```
2. Activate the newly created environment:
```sh
conda activate shopping-cart
```

2. Install the pandas, dotenv and sendgrid packages by running the following command:

```sh
pip install -r requirements.txt
```
3. Sign up for a Sendgrid account so that you can create a template and API key that will be used for sending the receipt via email:

3. Set up your own .env file that contains the tax rate for your locale:

```sh
TAX_RATE = 0.0875
```
modify the value of the TAX_RATE variable as needed

4. Create your products.csv file inside the data directory. The file structure should resemble the following:
```sh
id,name,aisle,department,price
1,Chocolate Sandwich Cookies,cookies cakes,snacks,3.5
2,All-Seasons Salt,spices seasonings,pantry,4.99
3,Robust Golden Unsweetened Oolong Tea,tea,beverages,2.49
4,Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce,frozen meals,frozen,6.99
5,Green Chile Anytime Sauce,marinades meat preparation,pantry,7.99
6,Dry Nose Oil,cold flu allergy,personal care,21.99
7,Pure Coconut Water With Orange,juice nectars,beverages,3.5
8,Cut Russet Potatoes Steam N' Mash,frozen produce,frozen,4.25
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

After downloading this repo, you\'ll need to