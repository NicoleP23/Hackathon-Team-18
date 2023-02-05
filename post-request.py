import requests

url = 'https://freepcis.gs1.org/server/Hackathon/capture'
print(url)
eventfile = open('./event.xml')

x = requests.post(url, data = eventfile)