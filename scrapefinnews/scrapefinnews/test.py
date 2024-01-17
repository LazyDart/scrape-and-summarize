import requests

response = requests.get(
  url='https://proxy.scrapeops.io/v1/',
  params={
      'api_key': 'aa1dd140-d5b7-4d00-a246-44f87d01c09a',
      'url': 'https://www.google.com/maps/place/Pizza+Saska+K%C4%99pa+Chicago%E2%80%99s+Pizza+Praga+Po%C5%82udnie+Praga+P%C3%B3%C5%82noc+Br%C3%B3dno+Goc%C5%82aw+Pizzeria/@52.2399092,21.0593349,17z/data=!3m1!5s0x471ecdb1dd93e7b5:0xaf4ac4ffd49930fb!4m16!1m7!3m6!1s0x471ecdb1c4a74c83:0x497e7215ad75dff8!2sPizza+Saska+K%C4%99pa+Chicago%E2%80%99s+Pizza+Praga+Po%C5%82udnie+Praga+P%C3%B3%C5%82noc+Br%C3%B3dno+Goc%C5%82aw+Pizzeria!8m2!3d52.2399092!4d21.0619098!16s%2Fg%2F1v6wn1sz!3m7!1s0x471ecdb1c4a74c83:0x497e7215ad75dff8!8m2!3d52.2399092!4d21.0619098!9m1!1b1!16s%2Fg%2F1v6wn1sz?entry=ttu' 
  },
)

print('Response Body: ', response.content)