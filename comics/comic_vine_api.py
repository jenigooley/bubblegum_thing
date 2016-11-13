import requests
import pprint
import json


def call_api(series, issue_number):
    headers = {
        'User-Agent': 'Chrome/53.0.2785.116',
        'From': 'jeni.gooley.42@gmail.com'
    }

    #issue_number = str(issue_number)
    payload = {
                'format': 'json',
               'api_key': '146a6f54ec76f2792d20444c54a16a0dcdb7b48b',
               'query': '"' + series + ' ' + issue_number + '"',
               'resources': 'issue, publisher, person'
}
    r = requests.get('http://comicvine.gamespot.com/api/search/',
                     headers=headers, params=payload)
    results = r.json()['results']
    pprint.pprint(results)
    return results


def get_issue(results, issue_number):
    # comic = [i.get('issue_number') for i in results]
    #issue_number = str(issue_number)
    for d in results:
        pprint.pprint(d)
        print issue_number
        if 'issue_number' in d:
            print('NUMBER', d['issue_number'])
            if d['issue_number'] == issue_number:
                print ('ISSUE', d)
                return d


def get_api_detail_url(issue):
    if issue:
        if issue.has_key('api_detail_url'):
            return issue['api_detail_url']
        elif issue.has_key(volume):
            return issue['volume']['api_detail_url']
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
                    'cover_art': issue_stats['image']['small_url'],
                    'series': issue_stats['volume']['name'],
                    'issue_title': issue_stats['name']
                    }

    if issue_stats.has_key('description') and issue_stats['description'] is not None:
        narrow_stats['description'] = (issue_stats['description']).strip('p><h4><i><em></i></em></p></i></p><h4>List of covers and their creators:</h4><table data-max-width="true"><thead><tr><th scope="col">Cover</th><th scope="col">Name</th><th scope="col">Creators</th><th scope="col">Sidebar Location</th></tr></thead><tbody><tr><td>Reg</td><td>Regular Cover</td><td>Fiona Staples</td><td>1</td></tr><tr><td>Var</td><td>C2E2 Diamond Retailer Summit 2012 Exclusive Variant (Limited to 500 copies)</td><td>Fiona Staples</td><td>Missing</td></tr><tr><td>2nd Print</td><td>Second Printing Cover</td><td>Fiona Staples</td><td>4</td></tr><tr><td>3rd Print</td><td>Third Printing Cover</td><td>Fiona Staples</td><td>3</td></tr><tr><td>4th Print</td><td>Fourth Printing Cover</td><td>Fiona Staples</td><td>Missing</td></tr><tr><td>5')

    else:
        narrow_stats['description'] = ' '
    if issue_stats.has_key('publisher') and issue_stats['publisher'] is not None:
        narrow_stats['publisher'] = issue_stats['publisher']
    else:
        narrow_stats['publisher'] = ' '
    if issue_stats.has_key('cover_date') and issue_stats['cover_date'] is not None:
        narrow_stats['cover_date'] = issue_stats['cover_date']
    else:
        narrow_stats['cover_date'] = ' '
    if issue_stats.has_key('writer'):
        narrow_stats['writer'] = issue_stats['writer']
    elif issue_stats.has_key('writer, cover'):
        narrow_stats['writer'] = issue_stats['writer, cover']
    else:
        narrow_stats['writer'] = ' '
    if issue_stats.has_key('letterer'):
        narrow_stats['letterer'] = issue_stats['letterer']
    elif issue_stats.has_key('letterer, other'):
        narrow_stats['letterer'] = issue_stats['letterer, other']
    else:
        narrow_stats['letterer'] = ' '
    if issue_stats.has_key('artist, colorist, cover'):
        narrow_stats['artist'] = issue_stats['artist, colorist, cover']
    elif issue_stats.has_key('artist, cover, other'):
        narrow_stats['artist'] = issue_stats['artist, cover, other']
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

def main(data, issue_number):
    issue_stats = {}
    issue_number = str(issue_number)
    results = call_api(data['series'], issue_number)
    issue = get_issue(results, issue_number)
    issue_url = get_api_detail_url(issue)
    persons = get_issue_persons(issue_url)
    credit = get_creater_credit(persons)
    issue_stats.update(issue)
    issue_stats.update(credit)
    pprint.pprint(issue_stats)
    narrow = narrow_results(issue_stats, issue_number)
    return narrow

if __name__ == '__main__':
    main()
