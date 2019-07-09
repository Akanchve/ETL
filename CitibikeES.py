import json
import requests
import datetime
import time
from pytz import timezone
from elasticsearch import Elasticsearch

r = requests.get("http://localhost:9200")
es = Elasticsearch([{"host": "localhost", "port":9200}])
print(r)
# i=1
while (True):
#while r.status_code == 200:
    r = requests.get("https://gbfs.citibikenyc.com/gbfs/en/station_status.json")
# print(r.content)
    data = json.loads(r.content)
    i=0
    for item in data['data']['stations']:
        temp = data["data"]["stations"][i]["last_reported"]
        #print (data["data"]["stations"][i])

        #test = json.loads(data["data"]["stations"][i])
        #print (test)
        #print(item)
        if temp != 18001:
            temp = datetime.datetime.fromtimestamp(temp)
            temp = temp.astimezone(timezone('UTC'))
            print (temp)
            data["data"]["stations"][i]["last_reported"] = temp
            es.index(index="citibiketest",doc_type="bike",body = data["data"]["stations"][i])
        #print(data["data"]["stations"][i]["last_reported"])
        i=i+1
    time.sleep(300)
    #es.index(index="citibiketest",doc_type="bike",body = data["data"])
    # i=i+1
