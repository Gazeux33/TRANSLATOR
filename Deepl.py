import requests
import json



# POST /v2/translate HTTP/2
# Host: api-free.deepl.com     {url}

# Authorization: DeepL-Auth-Key [yourAuthKey] 
# User-Agent: YourApp/1.2.3
# Content-Type: application/x-www-form-urlencoded      {headers}

# text=Hello%2C%20world!&target_lang=DE      {data}

with open("config.json","r") as file:
    data = json.load(file)


auth_key = data["auth_key"]

url = "https://api-free.deepl.com/v2/translate"

headers = {"Authorization": f"DeepL-Auth-Key {auth_key}",
           "User-Agent": "YourApp/1.2.3",
           "Content-Type": "application/x-www-form-urlencoded"}




def deepl_API(data):
    request = requests.post(url=url, headers=headers, data=data)
    if request.status_code == 200:
        return request.json()

    else:
        print("Une erreur s'est produite. Code de statut :", request.status_code)
