import urllib3
import logging as logger
import json

logger.basicConfig(level="DEBUG")

DD_API_KEY_NAME = "Example-Api-Key-Suraj-new1"

DD_URL = 'https://api.datadoghq.com/api/v2/api_keys'
#data = '{"data": {"type": "api_keys","attributes": {"name": {{DD_API_KEY_NAME}}}}}'

encoded_body = json.dumps({
  "data": {
    "type": "api_keys",
    "attributes": {
      "name": DD_API_KEY_NAME
    }
  }
})

headers = {"Accept": "application/json", "Content-Type": "application/json", "DD-API-KEY": "8f7032b242a646c71603fd368a0a7f6e", "DD-APPLICATION-KEY": "659222a35ddbbc2e0d48971f2e05b7065e41cafe"}


#http = urllib3.PoolManager()
#output = http.request('POST', DD_URL, headers={"Accept": "application/json", "Content-Type": "application/json", "DD-API-KEY": "8f7032b242a646c71603fd368a0a7f6e", "DD-APPLICATION-KEY": "659222a35ddbbc2e0d48971f2e05b7065e41cafe"},body=encoded_body)

#print(output.data)
def getDDApiKey(DD_URL, encoded_body):
  try:
    http = urllib3.PoolManager()
    output = http.request('POST', DD_URL,
                 headers=headers,
                 body=encoded_body) 
    #print(output.status_code)
    logger.info('Info message: The status code of this API call is {}'.format(output.status))
    #print(output.data)
    return output

  except urllib3.exceptions.HTTPError as errh:
    print ("Http Error:",errh)

try: 

  response = getDDApiKey(DD_URL,encoded_body)
  print(response.data)
  #print(response.data)
  #print("API Key is: {}".format(response["data"]["attributes"]["key"]))
  #print("API Key Name is: {}".format(response["data"]["attributes"]["name"]))

  if x.status_code == 201:
    print("All good")
  else:
    print("not good")
except:
    print ("something is wrong")