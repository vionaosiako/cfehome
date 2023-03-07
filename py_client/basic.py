import requests

# endpoints = "https://httbbin.org/status/200/"
# endpoints = "https://httbbin.org/"
endpoints = "http://127.0.0.1:8000/"

get_response = requests.get(endpoints, json={"query":"Hello world"})#API HTTP Request
print(get_response.text)#print raw text response
print(get_response.status_code)

