import requests

def handler(pd: "pipedream"):
  r = requests.get('https://swapi.dev/api/people/')
  # Export the data for use in future steps
  return r.json()
