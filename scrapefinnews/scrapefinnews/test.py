import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': 'aa1dd140-d5b7-4d00-a246-44f87d01c09a',
      'url': 'https://allegro.pl/,' 
  },
)

print('Response Body: ', response.content)