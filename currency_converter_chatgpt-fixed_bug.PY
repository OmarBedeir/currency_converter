import requests
import pycountry

# Get a list of all currency codes and names
currencies = {
    currency.alpha_3: currency.name
    for currency in pycountry.currencies
}

# Get the initial currency from the user
while True:
    init_currency = input("Enter an initial currency code: ")
    if init_currency not in currencies:
        print(f"Invalid currency code. Please try again.\n")
        continue
    break

# Get the target currency from the user
while True:
    target_currency = input("Enter a target currency code: ")
    if target_currency not in currencies:
        print(f"Invalid currency code. Please try again.\n")
        continue
    break

# Get the amount from the user
while True:
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            print("The amount must be greater than 0\n")
            continue
        break
    except ValueError:
        print("The amount must be a numeric value!\n")

# Make the API call
url = "https://api.apilayer.com/fixer/convert"
params = {
    "to": target_currency,
    "from": init_currency,
    "amount": amount
}
headers = {
    "apikey": "xczqFWwhlZIuKNhVXK2KD2ol8H55Vujw"
}

response = requests.get(url, params=params, headers=headers)

# Check the status of the response
if response.status_code != 200:
    print("Sorry, there was a problem. Please try again later.")
    quit()

# Extract the converted amount from the response
result = response.json()
converted_amount = result.get("result", 0)

# Print the result
print(f"{amount} {init_currency} is equal to {converted_amount} {target_currency}.")
