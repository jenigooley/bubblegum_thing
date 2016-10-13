import requests
import pprint

upc = raw_input('Enter UPC number: ')
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}
payload = {'upc':upc}
r = requests.get('https://api.upcitemdb.com/prod/trial/lookup', headers=headers, params=payload)

results = r.json()
pprint.pprint(results)
