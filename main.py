from hcapbypass import bypass
#import random, string, requests, json

sitekey = "f5561ba9-8f1e-40ca-9b5b-a0b3f719ef34"
#
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 #(KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#
#url_fingerprint = 'https://discord.com/api/v9/auth/fingerprint' # Get the fingerprint
#
#randomname = ''.join(random.choice(string.ascii_uppercase + string.digits + #string.ascii_lowercase)for _ in range(14))
#randomemail = ''.join(random.choice(string.ascii_uppercase + string.digits + #string.ascii_lowercase)for _ in range(5))
#email = f'{randomname}@{randomemail}.com'
#
#print(email)
#
#response = requests.post(url_fingerprint)
#fingerprint = json.loads(response.text)['fingerprint']
#print(fingerprint)
#print(response.text, "\n")
#
#Jsonn = {
#  'captcha_key': "range",
#  'consent': 'true',
#  'date_of_birth': f"2000-04-20",
#  'email': email,
#  'fingerprint': fingerprint,
#  'gift_code_sku_id': 'null',
#  'invite': 'nfDFu8pQ',
#  'password': "4567uhgTUHGTUY%^&",
#  'username':  "Test Here",
#}

bypass(sitekey, "discord.com", proxy="139.59.1.14:3128")
print(res)
#response = requests.post("https://discord.com/api/v9/auth/register", headers=headers, json=Jsonn) # Send the register request
#print(response.text)
