import firebase_admin
import json
from firebase_admin import credentials
from firebase_admin import firestore
from urllib.request import urlopen

project_id = "rent-me-1d154"

# Use the application default credentials
cred = credentials.Certificate('/Volumes/Local Disk/AppProjects/ProjectCredentials/rent-me-1d154-a4468d23ea36.json')
firebase_admin.initialize_app(cred, {
  'projectId': project_id,
})

db = firestore.client()

parseUrl1 = "http://api.data.go.kr/openapi/rntcarentrps-std?serviceKey=APIKEY&pageNo="
parseUrl2 = "&numOfRows=100&type=json"

for i in range(22):
    response = urlopen(parseUrl1 + str(i + 1) + parseUrl2).read().decode('utf-8')
    strJson = json.loads(response)

    for j in range(100):
        print(strJson.get("response").get("body").get("items")[j])

# doc_ref = db.collection(u'companies').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })