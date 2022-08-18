import requests
import logging as logger

logger.basicConfig(level="DEBUG")

url = 'HTTP://API.SHOUTCLOUD.IO/V1/SHOUT'
data = '{"INPUT": "hello world"}'

def getApiData(url, body):
  try:
    output = requests.post(url, data = data, headers = {"Content-Type": "application/json"})
    #print(output.status_code)
    logger.info('Info message: The status code of this API call is {}'.format(output.status_code))
    return output
  except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
  except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
    logger.error('Error message: There is issue connecting to this API address {}'.format(url))
  except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
  except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)

try: 

  x = getApiData(url,data)
  print(x.status_code)

  if x.status_code == 200:
    print("All good")
  else:
    print("not good")
except:
    print ("something is wrong")