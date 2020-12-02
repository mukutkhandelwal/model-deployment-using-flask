import requests

url = "http://localhost:5000/"

r = requests.post(url,json={'sentence':'it was really good flight'})

print(r.json())
