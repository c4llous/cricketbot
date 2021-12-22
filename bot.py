from urllib.request import urlopen
import json 
url = "https://hs-consumer-api.espncricinfo.com/v1/pages/matches/current?lang=en&latest=true"
data = urlopen(url)
data_json = json.loads(data.read())
print(data_json)
