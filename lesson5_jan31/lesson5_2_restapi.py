# pip install requests
import requests
res = requests.get('https://google.com')
if res.ok:
     print(res.content)


import json
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y["age"])


res = requests.get("https://api.exchangeratesapi.io/latest?base=USD")
data = res.json()
results = data['rates']
currency_value = results['ILS']
print("Result is: ", currency_value)


#post
# res = requests.post('http://127.0.0.1:5000/data/1', json={"user_name":"daniel"})
# if res.ok:
#     print(res.json())


#get
# res = requests.get('http://127.0.0.1:5000/data/2')
# if res.ok:
#     print(res.json())