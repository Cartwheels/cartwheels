from website import api_key, carts
import json, urllib2

def add_zips():
    for c in carts.find():
        try:
            data = urllib2.urlopen('http://maps.googleapis.com/maps/api/geocode/json?api_key%s&sensor=false&latlng=%f,%f' % (api_key, c.loc[0], c.loc[1]))
        except TypeError:
            continue

        try:
            data = json.loads(data.read())
            zip_code = data['results'][0]['address_components'][-1]['long_name']
            c.zip_code = zip_code
            c.save()
        except IndexError:
            continue
