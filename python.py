# # # # # # # # # # # # # # # # # # # #
# RESOLUTION LIFE AUSTRALASIA
# https://resolutionlife.com.au
#
# Description: An example of how to send log events to our API endpoint.
# # # # # # # # # # # # # # # # # # # #


# # # # # IMPORTS # # # # #
import requests


# # # # # GLOBALS # # # # #
API_KEY = "iJ9D3oHXARCmKK9FXAogEHZDAqahnDeS3Z4rUbjexzRdoSZx74qfxR9KxhSd7gg6546mDjyWSrAzsTiutLq4n3nVG4CgFVoryFHwLRxkUg42TAwrYTTJmKL96FWc8tZD"


# # # # # FUNCTIONS # # # #
def http_collector(api_key):
  headers = {
    "Authorization": api_key,
    "Content-Type": "text/plain"
  }
  
  body = "{'example1': 'test', 'timestamp': 1609100113039}"
  res = requests.post(url="https://resolutionlife.com.au/logs/v1/event",headers=headers,data=body)
  return res

if __name__ == "__main__":
  response = http_collector(API_KEY)
  print(response)
