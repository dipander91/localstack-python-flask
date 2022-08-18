import requests
import logging as logger
import json

logger.basicConfig(level="ERROR")

DD_API_KEY_NAME = "Example-Api-Key-Suraj-new1"

url = 'https://api.datadoghq.com/api/v2/api_keys'
#data = '{"data": {"type": "api_keys","attributes": {"name": {{DD_API_KEY_NAME}}}}}'

data = json.dumps({
  "data": {
    "type": "api_keys",
    "attributes": {
      "name": DD_API_KEY_NAME
    }
  }
})

def getDDApiKey(url, body):
  try:
    output = requests.post(url, data = data, headers = {"Accept": "application/json", "Content-Type": "application/json", "DD-API-KEY": "8f7032b242a646c71603fd368a0a7f6e", "DD-APPLICATION-KEY": "659222a35ddbbc2e0d48971f2e05b7065e41cafe"})
    #print(output.status_code)
    logger.info('Info message: The status code of this API call is {}'.format(output.status_code))
    return output
  except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)

try: 

  x = getDDApiKey(url,data)
  response = x.json()
  print("API Key is: {}".format(response["data"]["attributes"]["key"]))
  print("API Key Name is: {}".format(response["data"]["attributes"]["name"]))

  if x.status_code == 201:
    print("All good")
  else:
    print("not good")
except:
    print ("something is wrong")