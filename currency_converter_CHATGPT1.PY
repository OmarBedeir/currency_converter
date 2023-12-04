import requests
import matplotlib.pyplot as plt

def get_valid_currency_code(prompt, symbols):
    while True:
        currency_code = input(prompt).upper()
        if currency_code in symbols:
            return currency_code
        else:
            print("Invalid currency code. Please enter a valid code.")

def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                return amount
        except ValueError:
            print("Amount must be a numeric value.")

def fetch_currency_symbols(apikey):
    url = "https://api.apilayer.com/fixer/symbols"
    headers = {"apikey": apikey}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to fetch currency symbols. Status code: {response.status_code}")
        return []

    symbols_data = response.json()
    return symbols_data.get("symbols", {}).keys()

def convert_currency(init_currency, target_currency, amount, apikey):
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    headers = {"apikey": apikey}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Sorry, there was a problem. Status code: {response.status_code}")
        quit()

    result = response.json()
    if 'result' not in result:
        print(f"Error in API response: {result.get('error', 'Unknown error')}")
        quit()

    return result['result']

def display_conversion_graph(init_currency, target_currency, amount, converted_amount):
    labels = [init_currency, target_currency]
    values = [amount, converted_amount]

    plt.bar(labels, values, color=['blue', 'green'])
    plt.xlabel('Currency')
    plt.ylabel('Amount')
    plt.title('Currency Conversion')
    plt.show()

if __name__ == "__main__":
    apikey = "xczqFWwhlZIuKNhVXK2KD2ol8H55Vujw"
    symbols = fetch_currency_symbols(apikey)

    print("Commonly used currency codes for suggestions:", ", ".join(symbols))

    init_currency = get_valid_currency_code("Enter an initial currency: ", symbols)
    target_currency = get_valid_currency_code("Enter a target currency: ", symbols)
    amount = get_valid_amount()

    converted_amount = convert_currency(init_currency, target_currency, amount, apikey)

    print(f'{amount} {init_currency} = {converted_amount} {target_currency}')

    display_conversion_graph(init_currency, target_currency, amount, converted_amount)
