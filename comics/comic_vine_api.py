import requests
import pprint
import json


def call_api():
    headers = {
        'User-Agent': 'Chrome/53.0.2785.116',
        'From': 'jeni.gooley.42@gmail.com'
    }
    title = raw_input('Name of comic: ')
    issue_number = raw_input('Issue number: ')
    payload = { 'format': 'json',
                'api_key': '146a6f54ec76f2792d20444c54a16a0dcdb7b48b', 'query':'"' + title + '"',
                'resources': 'issue, publisher, person'}
    r = requests.get('http://comicvine.gamespot.com/api/search/', headers=headers, params=payload)

    results = r.json()['results']
    # pprint.pprint(results)
    return results, issue_number


def find_issue_number(results, issue_number):
    # comic = [i.get('issue_number') for i in results]
    for d in results:
        if 'issue_number' in d:
            if d['issue_number'] == issue_number:
                pprint.pprint(d)
                return d


def get_api_detail_url(issue):
    if issue.has_key('api_detail_url'):
        url = issue['api_detail_url']
        print ('URL: ', url)
        return url
    else:
        print 'api_detail_url not found'

def get_issue_persons(issue_url):
    headers = {
        'User-Agent': 'Chrome/53.0.2785.116',
        'From': 'jeni.gooley.42@gmail.com'
    }
    payload = { 'format': 'json',
                'api_key': '146a6f54ec76f2792d20444c54a16a0dcdb7b48b'
                 }

    r = requests.get(issue_url, headers=headers, params=payload)
    results = r.json()
    return results

def get_creater_credit(persons):
    credits = {}
    pprint.pprint(persons)
    for i in persons['results']['person_credits']:
        for k,v in i.items():
            if k == 'name' or k == 'role':
                credits[k]=[v]
        print credits




def main():
    results, issue_number = call_api()
    issue = find_issue_number(results, issue_number)
    issue_url = get_api_detail_url(issue)
    persons = get_issue_persons(issue_url)
    credit = get_creater_credit(persons)

if __name__ == '__main__':
    main()
