import requests
a = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text.split("</Valute>")
NAME = input(str("Введите валюту : "))
print(a.headers['Date'])
def currency_rates(NAME):
    for n in r:
        if n.count((NAME).upper()):
            nominal = (int(n[n.find('<Nominal>') + len('<Nominal>'):n.find('</Nominal>')]))
            value = (float(n[n.find('<Value>') + len('<Value>'):n.find('</Value>')].replace(',', '.')))
            print(f"{nominal} {NAME} равен {value} рублей")
    return
currency_rates(NAME)

if __name__ == '__main__':
    print(currency_rates('USD'))
