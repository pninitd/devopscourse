import requests

# Part 2 - API
# 1
def get_currency(cnt):
    res = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
    data = res.json()
    results = data['rates']
    currency_value = results[cnt]
    return currency_value


amount = float(input('Please enter an amount of Shekeles to convert to Dollars: '))
currency = get_currency('ILS')
print(currency*amount)

