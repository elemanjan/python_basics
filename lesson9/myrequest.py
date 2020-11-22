from requests import get

response = get("https://www.google.kg/")
print(response.text)
