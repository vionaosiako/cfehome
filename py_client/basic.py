import requests

endpoints = "https://httbbin.org/status/200/"
endpoints = "https://httbbin.org/"

get_response = requests.get()#API HTTP Request
print(get_response.text)#print raw text response