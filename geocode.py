import httplib2
import json

def geoLocationCode(inputString):
	api_key = "AIzaSyD0qOek_wU5bYBhhtRyVNAZC0kf1ojnTpM"
	location_string = inputString.replace(" ","+")
	url = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s'% (location_string,api_key))
	h = httplib2.Http()
	response, content = h.request(url,'GET')
	result = json.loads(content)
	return result