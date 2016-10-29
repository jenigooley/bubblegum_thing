import requests
import pprint
import json


def call_api(series, issue_title):
    headers = {
        'User-Agent': 'Chrome/53.0.2785.116',
        'From': 'jeni.gooley.42@gmail.com'
    }
    payload = {
                'format': 'json',
               'api_key': '146a6f54ec76f2792d20444c54a16a0dcdb7b48b',
               'query': '"' + series + ' ' + issue_title + '"',
               'resources': 'issue, publisher, person'
}
    r = requests.get('http://comicvine.gamespot.com/api/search/',
                     headers=headers, params=payload)
    results = r.json()['results']
    pprint.pprint(results)
    return results


def get_issue(results, issue_number):
    # comic = [i.get('issue_number') for i in results]
    for d in results:
        if 'issue_number' in d:
            if d['issue_number'] == issue_number:
                return d


def get_api_detail_url(issue):
    if issue.has_key('api_detail_url'):
        return issue['api_detail_url']
    else:
        print 'api_detail_url not found'


def get_issue_persons(issue_url):
    headers = {
        'User-Agent': 'Chrome/53.0.2785.116',
        'From': 'jeni.gooley.42@gmail.com'
    }
    payload = {
               'format': 'json',
               'api_key': '146a6f54ec76f2792d20444c54a16a0dcdb7b48b'
                }

    r = requests.get(issue_url, headers=headers, params=payload)
    return r.json()

def get_creater_credit(persons):
    return {i['role']: i['name']
            for i in persons['results']['person_credits']}


def narrow_results(issue_stats, issue_number):
    narrow_stats = {
                    'issue_number': issue_number,
                    'cover_date': issue_stats['cover_date'],
                    'cover_art': issue_stats['image']['super_url'],
                    'writer': issue_stats['writer'],
                    'publisher': 'Image',
                    'series': issue_stats['volume']['name'],
                    'issue_title': issue_stats['name'],
                    'description': (issue_stats['description']).strip('p><i></i></p>')
    }
    if issue_stats.has_key('letterer'):
        narrow_stats['letterer'] = issue_stats['letterer']
    elif issue_stats.has_key('letterer, other'):
        narrow_stats['letterer'] = issue_stats['letterer, other']
    else:
        narrow_stats['letterer'] = ' '
    if issue_stats.has_key('artist, colorist, cover'):
        narrow_stats['artist'] = issue_stats['artist, colorist, cover']
    elif issue_stats.has_key('artist, cover, other'):
        narrow_stats['artist'] = ['artist, cover, other']
    elif issue_stats.has_key('artist, cover'):
        narrow_stats['artist'] = issue_stats['artist, cover']
    elif issue_stats.has_key('artist, colorist'):
        narrow_stats['artist'] = issue_stats['artist, cover']
    elif issue_stats.has_key('artist'):
        narrow_stats['artist'] = issue_stats['artist']
    else:
        narrow_stats['artist'] = ' '
    pprint.pprint(narrow_stats)
    return narrow_stats

def main(data):
    issue_stats = {}
    results = call_api(data['series'], data['issue_title'])
    issue = get_issue(results, data['issue_number'])
    issue_url = get_api_detail_url(issue)
    persons = get_issue_persons(issue_url)
    credit = get_creater_credit(persons)
    issue_stats.update(issue)
    issue_stats.update(credit)
    pprint.pprint(issue_stats)
    narrow = narrow_results(issue_stats, data['issue_number'])
    return narrow

if __name__ == '__main__':
    main()
