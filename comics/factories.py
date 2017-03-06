from .models import *

import factory 

class ComicFactory(factory.Factory):
	FACTORY_FOR = Comic

	series = factory.Sequence(lambda n: 'series' + str(n))
	issue_number = factory.Sequence(lambda n: 'number' + str(n))
	issue_title = factory.Sequence(lambda n: 'title' + str(n))
	description = factory.Sequence(lambda n: 'decription' + str(n))
	cover_art = factory.Sequence(lambda n: 'cover_art' + str(n))
	writer = factory.Sequence(lambda n: 'writer' + str(n))
	artist = factory.Sequence(lambda n: 'writer' + str(n))
	letterer = factory.Sequence(lambda n: 'letterer' + str(n))
	publisher = factory.Sequence(lambda n: 'publisher' + str(n))
	cover_date = factory.Sequence(lambda n: 'cover_date' + str(n))

class Meta:
	model = Comic
	abstract = False

    # series = 'abc'
    # issue_number = '123'
    # issue_title = 'abc'
    # description = 'abc'
    # cover_art = 'image.com'
    # writer = 'abc'
    # artist = 'abc'
    # letterer = 'abc'
    # publisher = 'abc'
    # cover_date = '01-01-01'