import requests

url = 'https://freepcis.gs1.org/server/Hackathon/capture'
eventfile = open('./event.xml')
requests.post(url, data = eventfile)