import requests
for x in range(3):
    r = requests.get('https://webhook.site/6e55c3c9-95eb-4b1d-bffe-6518321f70ae')
    print(r.headers['Date'])
    