import sunlight
ny_legs = sunlight.openstates.legislators(state='ny')
for leg in ny_legs:
    print leg

leg.viewvalues
# OUT: <built-in method viewvalues of dict object at 0x257c560>
leg.viewvalues()
# OUT: dict_values([u'Little', u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'2012-12-12 17:30:32', u'Elizabeth Little', u'NYL000034', u'Elizabeth', u'', u'45', u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'ny', u'4342', u'Republican', u'http://www.nysenate.gov/files/imagecache/senator_teaser/profile-pictures/24x7%40300dpi.jpg', u'little@nysenate.gov', u'NYL000034', True, u'6531618d2b8d402c8bf7dc9d5f5d0d29', u'(518) 743-0968', u'(518) 455-2811', u'state', u'http://www.nysenate.gov/senator/elizabeth-little', u'us', u'2011-05-05 01:29:13', u'upper', [{u'fax': None, u'name': u'Capitol Office', u'phone': u'(518) 455-2811', u'address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'type': u'capitol', u'email': None}, {u'fax': None, u'name': u'District Office', u'phone': u'(518) 743-0968', u'address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'type': u'district', u'email': None}], u''])
leg.viewitems()
# OUT: dict_items([(u'last_name', u'Little'), (u'+capitol_address', u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247'), (u'updated_at', u'2012-12-12 17:30:32'), (u'full_name', u'Elizabeth Little'), (u'id', u'NYL000034'), (u'first_name', u'Elizabeth'), (u'middle_name', u''), (u'district', u'45'), (u'+district_address', u'5 Warren Street  Suite 3\nGlens Falls, NY 12801'), (u'state', u'ny'), (u'votesmart_id', u'4342'), (u'party', u'Republican'), (u'photo_url', u'http://www.nysenate.gov/files/imagecache/senator_teaser/profile-pictures/24x7%40300dpi.jpg'), (u'email', u'little@nysenate.gov'), (u'leg_id', u'NYL000034'), (u'active', True), (u'transparencydata_id', u'6531618d2b8d402c8bf7dc9d5f5d0d29'), (u'+district_phone', u'(518) 743-0968'), (u'+capitol_phone', u'(518) 455-2811'), (u'level', u'state'), (u'url', u'http://www.nysenate.gov/senator/elizabeth-little'), (u'country', u'us'), (u'created_at', u'2011-05-05 01:29:13'), (u'chamber', u'upper'), (u'offices', [{u'fax': None, u'name': u'Capitol Office', u'phone': u'(518) 455-2811', u'address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'type': u'capitol', u'email': None}, {u'fax': None, u'name': u'District Office', u'phone': u'(518) 743-0968', u'address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'type': u'district', u'email': None}]), (u'suffixes', u'')])
leg.items()
# OUT: [(u'last_name', u'Little'), (u'+capitol_address', u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247'), (u'updated_at', u'2012-12-12 17:30:32'), (u'full_name', u'Elizabeth Little'), (u'id', u'NYL000034'), (u'first_name', u'Elizabeth'), (u'middle_name', u''), (u'district', u'45'), (u'+district_address', u'5 Warren Street  Suite 3\nGlens Falls, NY 12801'), (u'state', u'ny'), (u'votesmart_id', u'4342'), (u'party', u'Republican'), (u'photo_url', u'http://www.nysenate.gov/files/imagecache/senator_teaser/profile-pictures/24x7%40300dpi.jpg'), (u'email', u'little@nysenate.gov'), (u'leg_id', u'NYL000034'), (u'active', True), (u'transparencydata_id', u'6531618d2b8d402c8bf7dc9d5f5d0d29'), (u'+district_phone', u'(518) 743-0968'), (u'+capitol_phone', u'(518) 455-2811'), (u'level', u'state'), (u'url', u'http://www.nysenate.gov/senator/elizabeth-little'), (u'country', u'us'), (u'created_at', u'2011-05-05 01:29:13'), (u'chamber', u'upper'), (u'offices', [{u'fax': None, u'name': u'Capitol Office', u'phone': u'(518) 455-2811', u'address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'type': u'capitol', u'email': None}, {u'fax': None, u'name': u'District Office', u'phone': u'(518) 743-0968', u'address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'type': u'district', u'email': None}]), (u'suffixes', u'')]
leg
# OUT: {u'last_name': u'Little', u'+capitol_address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'updated_at': u'2012-12-12 17:30:32', u'full_name': u'Elizabeth Little', u'id': u'NYL000034', u'first_name': u'Elizabeth', u'middle_name': u'', u'district': u'45', u'+district_address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'state': u'ny', u'votesmart_id': u'4342', u'party': u'Republican', u'photo_url': u'http://www.nysenate.gov/files/imagecache/senator_teaser/profile-pictures/24x7%40300dpi.jpg', u'email': u'little@nysenate.gov', u'leg_id': u'NYL000034', u'active': True, u'transparencydata_id': u'6531618d2b8d402c8bf7dc9d5f5d0d29', u'+district_phone': u'(518) 743-0968', u'+capitol_phone': u'(518) 455-2811', u'level': u'state', u'url': u'http://www.nysenate.gov/senator/elizabeth-little', u'country': u'us', u'created_at': u'2011-05-05 01:29:13', u'chamber': u'upper', u'offices': [{u'fax': None, u'name': u'Capitol Office', u'phone': u'(518) 455-2811', u'address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'type': u'capitol', u'email': None}, {u'fax': None, u'name': u'District Office', u'phone': u'(518) 743-0968', u'address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'type': u'district', u'email': None}], u'suffixes': u''}
leg.items()
# OUT: [(u'last_name', u'Little'), (u'+capitol_address', u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247'), (u'updated_at', u'2012-12-12 17:30:32'), (u'full_name', u'Elizabeth Little'), (u'id', u'NYL000034'), (u'first_name', u'Elizabeth'), (u'middle_name', u''), (u'district', u'45'), (u'+district_address', u'5 Warren Street  Suite 3\nGlens Falls, NY 12801'), (u'state', u'ny'), (u'votesmart_id', u'4342'), (u'party', u'Republican'), (u'photo_url', u'http://www.nysenate.gov/files/imagecache/senator_teaser/profile-pictures/24x7%40300dpi.jpg'), (u'email', u'little@nysenate.gov'), (u'leg_id', u'NYL000034'), (u'active', True), (u'transparencydata_id', u'6531618d2b8d402c8bf7dc9d5f5d0d29'), (u'+district_phone', u'(518) 743-0968'), (u'+capitol_phone', u'(518) 455-2811'), (u'level', u'state'), (u'url', u'http://www.nysenate.gov/senator/elizabeth-little'), (u'country', u'us'), (u'created_at', u'2011-05-05 01:29:13'), (u'chamber', u'upper'), (u'offices', [{u'fax': None, u'name': u'Capitol Office', u'phone': u'(518) 455-2811', u'address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'type': u'capitol', u'email': None}, {u'fax': None, u'name': u'District Office', u'phone': u'(518) 743-0968', u'address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'type': u'district', u'email': None}]), (u'suffixes', u'')]
leg()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: TypeError: 'dict' object is not callable
leg
# OUT: {u'last_name': u'Little', u'+capitol_address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'updated_at': u'2012-12-12 17:30:32', u'full_name': u'Elizabeth Little', u'id': u'NYL000034', u'first_name': u'Elizabeth', u'middle_name': u'', u'district': u'45', u'+district_address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'state': u'ny', u'votesmart_id': u'4342', u'party': u'Republican', u'photo_url': u'http://www.nysenate.gov/files/imagecache/senator_teaser/profile-pictures/24x7%40300dpi.jpg', u'email': u'little@nysenate.gov', u'leg_id': u'NYL000034', u'active': True, u'transparencydata_id': u'6531618d2b8d402c8bf7dc9d5f5d0d29', u'+district_phone': u'(518) 743-0968', u'+capitol_phone': u'(518) 455-2811', u'level': u'state', u'url': u'http://www.nysenate.gov/senator/elizabeth-little', u'country': u'us', u'created_at': u'2011-05-05 01:29:13', u'chamber': u'upper', u'offices': [{u'fax': None, u'name': u'Capitol Office', u'phone': u'(518) 455-2811', u'address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247', u'type': u'capitol', u'email': None}, {u'fax': None, u'name': u'District Office', u'phone': u'(518) 743-0968', u'address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801', u'type': u'district', u'email': None}], u'suffixes': u''}
pprint.pprint(leg)
# OUT: {u'+capitol_address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247',
# OUT:  u'+capitol_phone': u'(518) 455-2811',
# OUT:  u'+district_address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801',
# OUT:  u'+district_phone': u'(518) 743-0968',
# OUT:  u'active': True,
# OUT:  u'chamber': u'upper',
# OUT:  u'country': u'us',
# OUT:  u'created_at': u'2011-05-05 01:29:13',
# OUT:  u'district': u'45',
# OUT:  u'email': u'little@nysenate.gov',
# OUT:  u'first_name': u'Elizabeth',
# OUT:  u'full_name': u'Elizabeth Little',
# OUT:  u'id': u'NYL000034',
# OUT:  u'last_name': u'Little',
# OUT:  u'leg_id': u'NYL000034',
# OUT:  u'level': u'state',
# OUT:  u'middle_name': u'',
# OUT:  u'offices': [{u'address': u'188 State Street  Room 310, Legislative Office Building\nAlbany, NY 12247',
# OUT:                u'email': None,
# OUT:                u'fax': None,
# OUT:                u'name': u'Capitol Office',
# OUT:                u'phone': u'(518) 455-2811',
# OUT:                u'type': u'capitol'},
# OUT:               {u'address': u'5 Warren Street  Suite 3\nGlens Falls, NY 12801',
# OUT:                u'email': None,
# OUT:                u'fax': None,
# OUT:                u'name': u'District Office',
# OUT:                u'phone': u'(518) 743-0968',
# OUT:                u'type': u'district'}],
# OUT:  u'party': u'Republican',
# OUT:  u'photo_url': u'http://www.nysenate.gov/files/imagecache/senator_teaser/profile-pictures/24x7%40300dpi.jpg',
# OUT:  u'state': u'ny',
# OUT:  u'suffixes': u'',
# OUT:  u'transparencydata_id': u'6531618d2b8d402c8bf7dc9d5f5d0d29',
# OUT:  u'updated_at': u'2012-12-12 17:30:32',
# OUT:  u'url': u'http://www.nysenate.gov/senator/elizabeth-little',
# OUT:  u'votesmart_id': u'4342'}
