import requests
import pprint
import subprocess
import comic_vine_api


output = subprocess.check_output(['zbarimg', 'IMG_1380.JPG', '-q'])
print output
junk, upc = output.split(':')
print upc

headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}
payload = {'upc':upc}
r = requests.get('https://api.upcitemdb.com/prod/trial/lookup', headers=headers, params=payload)

results = r.json()
pprint.pprint(results)

comic_title =   results['items'][0]['title']
print comic_title
data = comic_title

headers = {
    'User-Agent': 'Chrome/53.0.2785.116',
    'From': 'jeni.gooley.42@gmail.com'
}
payload = {
            'format': 'json',
           'api_key': '146a6f54ec76f2792d20444c54a16a0dcdb7b48b',
           'query': '"' + data + '"',
           'resources': 'issue, publisher, person'
}
r = requests.get('http://comicvine.gamespot.com/api/search/',
                 headers=headers, params=payload)

results = r.json()['results']
pprint.pprint(results)
