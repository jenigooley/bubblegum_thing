
if issue_stats['artist, colorist, cover']:
    return narrow_stats['artist'] = issue_stats['artist, colorist, cover']
elif issue_stats['artist, colorist']:
    return narrow_stats['artist'] = issue_stats['artist, cover']
elif issue_stats['artist']:
    retunr narrow_stats['artist'] = issue_stats['artist']
else:
    retunr narrow_stats['artist'] = ' '
