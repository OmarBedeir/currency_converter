import requests
import matplotlib.pyplot as plt

def get_valid_currency_code(prompt):
    valid_currency_codes = [
        "AED", "AFN", "ALL", "AMD", "ANG", "AOA", "ARS", "AUD", "AWG", "AZN",
        "BAM", "BBD", "BDT", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BRL",
        "BSD", "BTN", "BWP", "BYN", "BZD", "CAD", "CDF", "CHF", "CLP", "CNY",
        "COP", "CRC", "CUP", "CVE", "CZK", "DJF", "DKK", "DOP", "DZD", "EGP",
        "ERN", "ETB", "EUR", "FJD", "FKP", "FOK", "GBP", "GEL", "GGP", "GHS",
        "GIP", "GMD", "GNF", "GTQ", "GYD", "HKD", "HNL", "HRK", "HTG", "HUF",
        "IDR", "ILS", "IMP", "INR", "IQD", "IRR", "ISK", "JEP", "JMD", "JOD",
        "JPY", "KES", "KGS", "KHR", "KID", "KRW", "KWD", "KYD", "KZT", "LAK",
        "LBP", "LKR", "LRD", "LSL", "LYD", "MAD", "MDL", "MGA", "MKD", "MMK",
        "MNT", "MOP", "MRU", "MUR", "MVR", "MWK", "MXN", "MYR", "MZN", "NAD",
        "NGN", "NIO", "NOK", "NPR", "NZD", "OMR", "PAB", "PEN", "PGK", "PHP",
        "PKR", "PLN", "PYG", "QAR", "RON", "RSD", "RUB", "RWF", "SAR", "SBD",
        "SCR", "SDG", "SEK", "SGD", "SHP", "SLL", "SOS", "SPL", "SRD", "STN",
        "SYP", "SZL", "THB", "TJS", "TMT", "TND", "TOP", "TRY", "TTD", "TVD",
        "TWD", "TZS", "UAH", "UGX", "USD", "UYU", "UZS", "VES", "VND", "VUV",
        "WST", "XAF", "XCD", "XDR", "XOF", "XPF", "YER", "ZAR", "ZMW", "ZWL"
    ]

    while True:
        currency_code = input(prompt).upper()
        if currency_code in valid_currency_codes:
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

def convert_currency(init_currency, target_currency, amount):
    url = f"https://api.apilayer.com/fixer/convert?to={target_currency}&from={init_currency}&amount={amount}"
    headers = {"apikey": "xczqFWwhlZIuKNhVXK2KD2ol8H55Vujw"}

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
    init_currency = get_valid_currency_code("Enter an initial currency: ")
    target_currency = get_valid_currency_code("Enter a target currency: ")
    amount = get_valid_amount()

    converted_amount = convert_currency(init_currency, target_currency, amount)

    print(f'{amount} {init_currency} = {converted_amount} {target_currency}')

    display_conversion_graph(init_currency, target_currency, amount, converted_amount)
