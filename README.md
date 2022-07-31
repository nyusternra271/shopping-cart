# shopping-caart
Shopping Cart Project

## Introduction

This application prompts you to select from a group of products and presents a receipt for all of the goods
you've selected. It will also send a copy of the receipt via email.

## Requirements:

1. Create a new environment for running this program as follows:

```sh
conda create -n shopping-cart python=3.10
```
2. Activate the newly created environment:
```sh
conda activate shopping-cart
```

2. Install the pandas and dotenv packages by running the following command:

```sh
pip install -r requirements.txt
```
3. Set up your own .env file that contains the tax rate for your locale:

```sh
TAX_RATE = 0.0875

modify the value of the TAX_RATE variable as needed